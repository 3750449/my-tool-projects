# 🛡️ Phishing Detector (Flask + Machine Learning)

A web-based phishing detection app that uses a machine learning model to classify email messages as **phishing** or **legitimate** in real time. The system features adaptive retraining using user feedback and supports real email file uploads.

---

## 🚀 Features

- ✅ Logistic Regression + TF-IDF classification
- ✅ Flask web API with interactive frontend
- ✅ User feedback logging and adaptive model updates
- ✅ Upload and analyze `.eml` email files (e.g., Gmail, Outlook exports)
- ✅ Supports real-time predictions with confidence scores
- ✅ Easy deployment with Python and pip

---

## 📁 Project Structure

```
phishing-detector/
├── app.py                    # Flask app for API and web UI
├── phishing_detector.py      # Training script with feedback and .eml support
├── phishing_model.pkl        # Saved ML model (auto-generated)
├── dataset/
│   └── phishing_emails.csv   # Base labeled dataset
├── phishing_eml/             # Folder for phishing .eml files
├── legit_eml/                # Folder for legitimate .eml files
├── feedback_log.csv          # User feedback (auto-generated)
├── templates/
│   └── index.html            # Web interface
└── README.md                 # This file
```

---

## 💻 How to Run

1. Install dependencies (inside a virtual environment recommended):

```bash
pip install flask pandas scikit-learn joblib
```

2. Start the web app:

```bash
python app.py
```

3. Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🔁 How to Retrain with New Data

```bash
python phishing_detector.py
```

This will:
- Load the base dataset
- Include all feedback in `feedback_log.csv`
- Add `.eml` files from `phishing_eml/` and `legit_eml/`
- Train and save a new `phishing_model.pkl`

---

## 📦 File Upload Support

Upload `.eml` email files directly through the interface. The app will:
- Parse the email body
- Classify it using the trained model
- Show result + confidence

---

## ✨ Contributing

Contributions welcome! You can:
- Add new email samples
- Improve the model
- Extend support for `.msg` (Outlook) files
- Deploy it using Docker or to the cloud

---

## 📜 License

MIT License. For educational and research use.
