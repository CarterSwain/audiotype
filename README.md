## ⚠️ Note on Spotify API Changes

As of **November 27, 2024**, Spotify has officially deprecated and restricted access to the `/v1/audio-features` endpoint, which this project relied on to extract features like `tempo`, `danceability`, and `valence` for classification.

This means that **real-time analysis of a user's Spotify tracks is no longer possible** using Spotify's public API.

---

## 🧠 What Still Works

Despite the Spotify limitations, this project still includes:

- A **fully trained multi-class classification model** that maps audio features to custom personality types ("AudioTypes").
- A clean and extensible **Flask app** that handles Spotify OAuth login and retrieves user track metadata.
- Well-organized datasets (`/data`) and a working ML training pipeline (`train_model.py`).
- A saved model (`audiotype_model.pkl`) and scaler ready for use on any compatible dataset.

---

## 🛠️ Future Directions

You can still adapt or build on this project by:

- Using **cached or open-source Spotify datasets** (e.g. OpenSpotify, Million Song Dataset)
- Allowing users to **upload their own audio** and analyzing it with tools like `librosa`
- Repurposing the model to classify other types of creative content (art, writing, etc.)

---

## 🙏 Gratitude

This project remains a valuable experiment in building intelligent music-based personality models — and a reminder that APIs change, but what you build with them still matters.


# 🎧 AudioType

AudioType is a machine learning-powered app that analyzes a user's Spotify listening data and classifies them into one of 5 unique **AudioTypes** — musical personality profiles that reflect how they move, create, explore, and feel through music.

---

## Features

- **Spotify Login**: Authenticates users and pulls their saved tracks via the Spotify API.
- **Personality Classification**: Uses trained ML models to classify each track into an "AudioType".
- **Data-Driven Insights**: Visual breakdown of your listening personality.
- **5 AudioTypes**
  - The Stargazer
  - The Mender
  - The Kinetik
  - The Composer
  - The Seeker

---

## How It Works

1. User logs in with Spotify.
2. App fetches audio features (energy, valence, danceability, etc.) from their saved tracks.
3. A trained `RandomForestClassifier` predicts the AudioType for each track.
4. Results are aggregated into a visual personality profile.

---

## Tech Stack

- **Python** + **Scikit-learn** (ML)
- **Pandas** for data wrangling
- **Spotipy** (Spotify API wrapper)
- **Flask** for backend (coming soon)
- **PostgreSQL** (user data)
- **React** (frontend, coming soon)

---



