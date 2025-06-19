import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
df = pd.read_csv("mental_health_and_technology_usage_2024.csv")

# Encode categorical targets
mental_health_encoder = LabelEncoder()
stress_level_encoder = LabelEncoder()

df["Mental_Health_Status_Encoded"] = mental_health_encoder.fit_transform(df["Mental_Health_Status"])
df["Stress_Level_Encoded"] = stress_level_encoder.fit_transform(df["Stress_Level"])

# Select features and targets
features = [
    "Technology_Usage_Hours",
    "Social_Media_Usage_Hours",
    "Gaming_Hours",
    "Screen_Time_Hours",
    "Sleep_Hours",
    "Physical_Activity_Hours"
]

X = df[features]
y_mental = df["Mental_Health_Status_Encoded"]
y_stress = df["Stress_Level_Encoded"]

# Train models
mental_health_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])
stress_level_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

mental_health_model.fit(X, y_mental)
stress_level_model.fit(X, y_stress)

# Save models and encoders
joblib.dump(mental_health_model, "mental_health_model.pkl")
joblib.dump(stress_level_model, "stress_level_model.pkl")
joblib.dump(mental_health_encoder, "mental_health_encoder.pkl")
joblib.dump(stress_level_encoder, "stress_level_encoder.pkl")

print("✅ Models and encoders have been saved successfully.")
