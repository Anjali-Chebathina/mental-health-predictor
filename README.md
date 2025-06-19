
# 🧠 Mental Health & Stress Predictor

A machine learning-powered web app that predicts a user's mental health status and stress level based on their digital behavior — such as screen time, social media use, gaming hours, sleep, and physical activity.

---

## 🚀 Features

- 📊 Predicts **mental health status** and **stress level**
- 📱 Takes input on screen time, tech use, sleep, activity, etc.
- 🤖 Powered by machine learning (scikit-learn)
- 🌐 Frontend built with HTML/CSS and vanilla JavaScript
- 🔥 Flask-based backend with REST API
- 🧾 Clean UI with labels and validation
- 🔒 CORS enabled for cross-origin access

---

## 🛠️ Tech Stack

| Frontend      | Backend       | ML / Tools         |
|---------------|----------------|--------------------|
| HTML5, CSS3   | Python 3.11    | scikit-learn, joblib |
| JavaScript    | Flask + CORS   | RandomForest, Pipelines |
| Responsive UI | REST API       | NumPy              |

---

## 🖼️ Screenshots
![Screenshot 2025-06-19 223145](https://github.com/user-attachments/assets/bde576f8-4cab-4ee7-8164-e0dbce4e9a4a)


![Screenshot 2025-06-19 223034](https://github.com/user-attachments/assets/a7769344-358f-4176-ac94-0144ba806178)

---

## 🧪 How It Works

1. User enters screen time, gaming hours, sleep, activity, etc.
2. Data is sent via REST API to the Flask backend.
3. Trained ML models predict:
   - **Mental Health Status** (e.g., Healthy, Depressed)
   - **Stress Level** (e.g., High, Low)
4. Results are displayed instantly on the UI.

---

## 📦 Project Structure

```
mental-health-project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── mental_health_model.pkl
│   ├── stress_level_model.pkl
│   ├── mental_health_encoder.pkl
│   ├── stress_level_encoder.pkl
│
├── frontend/
│   ├── index.html

```

---

## 🧰 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Anjali-Chebathina/mental-health-predictor.git
cd mental-health-predictor/backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Flask backend

```bash
python app.py
```

> 🟢 The server will start at `http://127.0.0.1:5001`

### 5. Open the frontend

- Open `frontend/index.html` in your browser
- Fill the form
- Get predictions!

---

## 📝 Model Info

- Trained using scikit-learn 1.7.0
- Models used:
  - `RandomForestClassifier`
  - `DecisionTreeClassifier`
- LabelEncoders and StandardScaler are saved with `joblib`

---

## ❗ Warning

You may see:

```
InconsistentVersionWarning: Trying to unpickle estimator from version 1.7.0
```

> This is **safe to ignore**, as long as predictions work correctly.


---

## 🙌 Acknowledgments

- [Scikit-learn](https://scikit-learn.org)
- [Flask](https://flask.palletsprojects.com/)
- [Python](https://www.python.org/)
