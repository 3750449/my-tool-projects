

# phishing_detector.py

import os
import pandas as pd
import email
from email import policy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# === Helper: Load .eml emails ===
def extract_emails_from_eml_folder(folder_path, label):
    rows = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".eml"):
                try:
                    with open(os.path.join(root, file), "rb") as f:
                        msg = email.message_from_binary_file(f, policy=policy.default)
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body += part.get_content()
                        else:
                            body = msg.get_content()
                        body = body.strip()
                        if body:
                            rows.append({"email_content": body, "label": label})
                except Exception:
                    continue
    return pd.DataFrame(rows)

# === Step 1: Load CSV dataset ===
data = pd.read_csv("dataset/phishing_emails.csv")

# === Step 2: Load feedback log ===
try:
    feedback = pd.read_csv("feedback_log.csv", header=None, names=["timestamp", "email_content", "is_correct"])
    feedback["label"] = feedback["is_correct"].apply(lambda x: 1 if str(x).lower() == "false" else 0)
    feedback_data = feedback[["email_content", "label"]]
    data = pd.concat([data, feedback_data], ignore_index=True)
    print(f"✔️ Loaded {len(feedback_data)} feedback samples.")
except Exception as e:
    print("⚠️ No feedback data loaded:", e)

# === Step 3: Load .eml data ===
phishing_eml = extract_emails_from_eml_folder("phishing_eml", label=1)
legit_eml = extract_emails_from_eml_folder("legit_eml", label=0)
data = pd.concat([data, phishing_eml, legit_eml], ignore_index=True)
print(f"📥 Loaded {len(phishing_eml)} phishing and {len(legit_eml)} legit emails from .eml files.")

# === Step 4: Clean dataset ===
data = data.dropna(subset=["email_content", "label"])
data["email_content"] = data["email_content"].astype(str)

# === Step 5: Split data ===
X = data["email_content"]
y = data["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 6: Train model ===
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000)),
])
model.fit(X_train, y_train)

# === Step 7: Evaluate and Save ===
predictions = model.predict(X_test)
print("📊 Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
joblib.dump(model, "phishing_model.pkl")
print("✅ Model updated and saved.")
