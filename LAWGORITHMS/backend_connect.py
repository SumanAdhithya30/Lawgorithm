from flask import Flask, request, jsonify
import joblib
import os
from flask_cors import CORS #import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow calls from your React frontend

# Define file paths for the saved model and vectorizer
MODEL_PATH = "data/processed/model.pkl"
VECTORIZER_PATH = "data/processed/vectorizer.pkl"

def load_model_and_vectorizer():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(
            "Model or vectorizer file not found in data/processed/. Please run your training script to generate and save them."
        )
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if "summary" not in data:
        return jsonify({"error": "No 'summary' field provided in JSON data"}), 400

    case_summary = data["summary"]
    X = vectorizer.transform([case_summary])
    prediction = model.predict(X)
    result = "Winnable" if prediction[0] == 1 else "Not Winnable"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
