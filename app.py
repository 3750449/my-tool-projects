

# app.py

from flask import Flask, request, jsonify, render_template
import joblib
import csv
from datetime import datetime

import email
from email import policy

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    content = data.get("content", "")

    if not content.strip():
        return jsonify({"error": "No content provided"}), 400

    prediction = model.predict([content])[0]
    probability = max(model.predict_proba([content])[0])

    result = "Phishing" if prediction == 1 else "Legitimate"
    return jsonify({'result': result, 'probability': probability})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    content = data.get("content", "")
    is_correct = data.get("isCorrect", True)

    with open("feedback_log.csv", "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.utcnow(), content, is_correct])

    return jsonify({"status": "success"})


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    msg = email.message_from_bytes(uploaded_file.read(), policy=policy.default)

    # Extract the plain text body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                try:
                    body += part.get_content().strip()
                except:
                    continue
    else:
        try:
            body = msg.get_content().strip()
        except:
            return jsonify({'error': 'Could not read email content'}), 400

    if not body:
        return jsonify({'error': 'Email has no readable text'}), 400

    prediction = model.predict([body])[0]
    probability = max(model.predict_proba([body])[0])
    result = "Phishing" if prediction == 1 else "Legitimate"

    return jsonify({'result': result, 'probability': probability})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
