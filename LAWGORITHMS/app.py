# from flask import Flask, request, jsonify
# import joblib
# import os

# # Initialize the Flask application
# app = Flask(__name__)

# # Define file paths for the saved model and vectorizer
# MODEL_PATH = "model.pkl"
# VECTORIZER_PATH = "vectorizer.pkl"

# # Load the model and vectorizer; ensure these files exist!
# if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
#     raise FileNotFoundError("Model or vectorizer file not found in data/processed/")

# model = joblib.load(MODEL_PATH)
# vectorizer = joblib.load(VECTORIZER_PATH)

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get JSON data from the request
#     data = request.get_json(force=True)
#     # Validate that the 'summary' field is provided
#     if "summary" not in data:
#         return jsonify({"error": "No 'summary' field provided in JSON data"}), 400

#     case_summary = data["summary"]
#     # Transform the summary using the TF-IDF vectorizer
#     X = vectorizer.transform([case_summary])
#     # Predict using the logistic regression model
#     prediction = model.predict(X)
#     # Map prediction to a human-readable label
#     result = "Winnable" if prediction[0] == 1 else "Not Winnable"

#     # Return the prediction as JSON
#     return jsonify({"prediction": result})

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Define file paths for the saved model and vectorizer
MODEL_PATH = "data/processed/model.pkl"
VECTORIZER_PATH = "data/processed/vectorizer.pkl"

def load_model_and_vectorizer():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        # If files are missing, raise an error with instructions
        raise FileNotFoundError(
            "Model or vectorizer file not found in data/processed/. "
            "Please run your training script to generate and save them."
        )
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer

# Load the model and vectorizer
model, vectorizer = load_model_and_vectorizer()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Check if the 'summary' field is provided
    if "summary" not in data:
        return jsonify({"error": "No 'summary' field provided in JSON data"}), 400

    case_summary = data["summary"]
    
    # Transform the case summary using the TF-IDF vectorizer
    X = vectorizer.transform([case_summary])
    
    # Predict using the logistic regression model
    prediction = model.predict(X)
    
    # Convert prediction to a human-readable label
    result = "Winnable" if prediction[0] == 1 else "Not Winnable"
    
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

