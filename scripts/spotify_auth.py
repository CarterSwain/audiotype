from flask import Flask, redirect, request, session, url_for
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os
from dotenv import load_dotenv
import joblib
import numpy as np
from collections import Counter
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

SCOPE = "user-library-read"

auth_manager = SpotifyOAuth(
    scope=SCOPE,
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    show_dialog=True,
    cache_path=".spotifycache"
)

@app.route('/')
def login():
    auth_url = auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # SpotifyOAuth will handle token retrieval and caching automatically
    return redirect(url_for("get_audio_types"))

@app.route('/get_audio_types')
def get_audio_types():
    token_info = auth_manager.get_cached_token()
    if not token_info or "access_token" not in token_info:
        return redirect('/')

    access_token = token_info["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.current_user_saved_tracks(limit=20)
        track_ids = [item["track"]["id"] for item in results["items"] if item["track"] and item["track"]["id"]]

        # Call audio features
        features = sp.audio_features(track_ids)


        # Load trained model and scaler
        model = joblib.load("models/audiotype_model.pkl")
        scaler = joblib.load("models/scaler.pkl")

        predictions = []
        for feat in features:
            if feat is None:
                continue
            input_data = np.array([[
                feat["energy"],
                feat["tempo"],
                feat["instrumentalness"],
                feat["acousticness"],
                feat["danceability"],
                feat["valence"]
            ]])
            scaled = scaler.transform(input_data)
            prediction = model.predict(scaled)[0]
            predictions.append(prediction)

        if not predictions:
            return "Could not extract audio features."

        counter = Counter(predictions)
        dominant = counter.most_common(1)[0][0]

        response = f"<h2>Your dominant AudioType is: <b>{dominant}</b></h2><br>"
        response += "<h3>Breakdown:</h3>"
        for label, count in counter.items():
            response += f"{label}: {count} tracks<br>"

        return response

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)


