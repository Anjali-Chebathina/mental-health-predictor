import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load models
mental_model = joblib.load("mental_health_model.pkl")
stress_model = joblib.load("stress_level_model.pkl")
mental_encoder = joblib.load("mental_health_encoder.pkl")
stress_encoder = joblib.load("stress_level_encoder.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    try:
        features = np.array([
            data["Technology_Usage_Hours"],
            data["Social_Media_Usage_Hours"],
            data["Gaming_Hours"],
            data["Screen_Time_Hours"],
            data["Sleep_Hours"],
            data["Physical_Activity_Hours"]
        ]).reshape(1, -1)

        mental_pred = mental_model.predict(features)
        stress_pred = stress_model.predict(features)

        mental_label = mental_encoder.inverse_transform(mental_pred)[0]
        stress_label = stress_encoder.inverse_transform(stress_pred)[0]

        return jsonify({
            "mental_health_status": mental_label,
            "stress_level": stress_label
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=5001)
