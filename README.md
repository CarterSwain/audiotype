# 🎧 AudioType

AudioType is a machine learning-powered app that analyzes a user's Spotify listening data and classifies them into one of 5 unique **AudioTypes** — musical personality profiles that reflect how they move, create, explore, and feel through music.

---

## Features

- **Spotify Login**: Authenticates users and pulls their saved tracks via the Spotify API.
- **Personality Classification**: Uses trained ML models to classify each track into an "AudioType".
- **Data-Driven Insights**: Visual breakdown of your listening personality.
- **20 AudioTypes**, grouped into five musical families:
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



