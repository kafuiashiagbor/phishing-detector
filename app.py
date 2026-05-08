from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])

def predict():
    data = request.get_json()

    df = pd.DataFrame([data])
    prediction = model.predict(df)
    result = "phishing" if prediction[0] == 1 else "legitimate"
    return jsonify({"prediction": result})



if __name__ == "__main__":
    
    app.run(debug=True)