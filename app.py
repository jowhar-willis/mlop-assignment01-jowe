from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("alz_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    prediction = model.predict([data])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)