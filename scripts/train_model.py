import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
import os

# === Load Cleaned Datasets ===
data_dir = "data"
audio_types = [
    "composer_tracks.csv",
    "mender_songs.csv",
    "seeker_songs.csv",
    "stargazer_songs.csv",
    "kinetik_songs.csv"
]

dfs = []
for file in audio_types:
    path = os.path.join(data_dir, file)
    df = pd.read_csv(path)
    dfs.append(df)

# Combine all datasets
df = pd.concat(dfs, ignore_index=True)

# === Prepare Features and Labels ===
X = df.drop("label", axis=1)
y = df["label"]

# === Normalize Features ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)

# === Train Classifier ===
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# === Evaluate ===
y_pred = clf.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# === Save Model and Scaler ===
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/audiotype_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel and scaler saved to /models directory.")
