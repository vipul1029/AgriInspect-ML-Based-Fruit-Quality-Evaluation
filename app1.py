# Import Libraries
import os
import numpy as np
import pickle
from flask import Flask, request, render_template

# Flask App Initialization
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Load ML Model
MODEL_PATH = "best.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    return render_template("inner-page.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Read form inputs
    input_features = [int(float(x)) for x in request.form.values()]
    input_features = np.array([input_features])

    # Prediction
    prediction = model.predict(input_features)[0]

    result = "Good" if int(prediction) == 1 else "Bad"

    return render_template("output.html", result=result)

# Render Deployment Entry Point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2000))
    app.run(host="0.0.0.0", port=port)
