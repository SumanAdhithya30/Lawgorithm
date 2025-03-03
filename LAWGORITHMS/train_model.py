import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Define file paths
DATASET_PATH = "synthetic_case_winnability.csv"  # Adjust if your CSV is in a different location
MODEL_DIR = "data/processed"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# Load the synthetic dataset
df = pd.read_csv(DATASET_PATH)

# Map labels: "Winnable" -> 1, "Not Winnable" -> 0
df["Winnable_Label"] = df["Winnable"].map({"Winnable": 1, "Not Winnable": 0})

# Use "Case Summary" as features and the mapped label as the target
X = df["Case Summary"]
y = df["Winnable_Label"]

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer and transform the text data
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialize and train the Logistic Regression model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = clf.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("Classification Report:\n", report)

# Ensure the output directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Save the trained model and vectorizer using joblib
joblib.dump(clf, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)
print(f"Model and vectorizer saved successfully in '{MODEL_DIR}'.")
