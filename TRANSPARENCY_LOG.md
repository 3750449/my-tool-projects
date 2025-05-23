# 📜 Transparency Log

This document tracks the development, decisions, and changes made to the **Phishing Detection Web App** for public visibility and reproducibility.

---

## 🛠️ Project Purpose

To build a deployable web application that uses machine learning to detect phishing messages in real-time, accessible through a simple UI. It combines Python (Flask + scikit-learn) and front-end HTML/JavaScript.

---

## 📅 Development Timeline

### ✅ May 20, 2025 — Initial Setup

- Created Python virtual environment and installed packages:
  - `pandas`, `scikit-learn`, `nltk`, `joblib`
- Assembled a small CSV dataset `phishing_emails.csv` with example phishing and legitimate messages.
- Wrote `phishing_detector.py` to:
  - Load CSV
  - Train a logistic regression model using TF-IDF
  - Evaluate performance
  - Save model as `phishing_model.pkl`

---

### ✅ May 20, 2025 — Model Evaluation Fix

- Accuracy issues discovered due to tiny dataset.
- Expanded dataset with 16 balanced examples (8 phishing, 8 legitimate).
- Accuracy improved on retrain.

---

### ✅ May 20, 2025 — Backend Setup

- Created `app.py` using Flask to:
  - Load saved model
  - Provide `/detect` POST API
  - Serve `index.html` via root route

---

### ✅ May 20, 2025 — Frontend Setup

- Created `/templates/index.html` for UI
- Implemented:
  - Textarea input for email content
  - JS-based fetch request to `/detect`
  - Display of detection result and probability

---

### ✅ May 20, 2025 — App Operational

- Flask app successfully launched at `http://localhost:5000`
- Confirmed model working with UI and API

---

## 🧾 Decisions & Justifications

- **Logistic Regression** chosen for simplicity and explainability.
- **TF-IDF** used as vectorizer due to strong performance on short text classification.
- **Flask** selected for lightweight API and templating.
- **No deep learning** used to keep deployment minimal and portable.

---

## 📂 Directory Structure

```
phishing-detector/
├── app.py
├── phishing_detector.py
├── phishing_model.pkl
├── dataset/
│   └── phishing_emails.csv
├── templates/
│   └── index.html
└── TRANSPARENCY_LOG.md
```

---

## 🔜 Planned Next Steps

- [ ] Add logging to detect requests for audit
- [ ] Create Dockerfile for deployment
- [ ] Improve dataset size and diversity
- [ ] Implement better error handling and validation
- [ ] Write unit and integration tests

---

## ✨ ChatGPT Assistance Disclosure

This project was developed in collaboration with **OpenAI's ChatGPT-4-turbo**, used as a coding assistant for:

- 🧠 Ideation and architecture planning
- 📦 Code generation (training script, Flask API, frontend, Docker)
- 🛠️ Troubleshooting errors and improving dataset quality
- 📋 Writing this transparency log

ChatGPT was not used to generate training data or make model predictions. All model training was performed locally on curated and manually reviewed datasets.

**Why use ChatGPT?**

- Accelerated prototyping
- Helped break down complex steps
- Provided real-time debugging advice and example code
- Served as an educational aid throughout

**Human oversight** was maintained for:
- Reviewing and editing all AI-generated code
- Dataset preparation and quality control
- Final deployment decisions

This documentation was also collaboratively written with ChatGPT, with the user curating, approving, and formatting the final version.

---

## 📦 New Feature: .eml File Training Support (May 21, 2025)

The phishing detection system now supports extracting training data from `.eml` email files.

### How It Works:
- Automatically scans two directories:
  - `phishing_eml/` → labeled as Phishing (1)
  - `legit_eml/` → labeled as Legitimate (0)
- Parses text from each `.eml` file using Python’s email library
- Combines with:
  - Original CSV dataset (`phishing_emails.csv`)
  - Logged user feedback (`feedback_log.csv`)
- Trains the model using all three data sources.

This allows security teams and researchers to easily expand the model with real-world messages exported from Gmail, Outlook, Thunderbird, etc.
