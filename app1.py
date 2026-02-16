# ================================
# Import Libraries
# ================================
import os
import numpy as np
from flask import Flask, request, render_template
from xgboost import XGBClassifier

# ================================
# Flask App Initialization
# ================================
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ================================
# Load Trained XGBoost Model
# ================================
MODEL_PATH = "best.json"   # MUST be best.json

model = XGBClassifier()
model.load_model(MODEL_PATH)

# ================================
# Routes
# ================================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    return render_template("inner-page.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        # Read inputs (ORDER MUST MATCH FORM)
        features = [float(x) for x in request.form.values()]
        size, weight, sweetness, crunch, juice, ripe, acid = features

        # ==================================
        # RULE-BASED OVERRIDE (HARD LOGIC)
        # ==================================
        if (
            sweetness < 2.5 or
            crunch < 2.5 or
            juice < 2.5 or
            acid > 8.5 or
            ripe < 3.0
        ):
            result = "Bad"
            confidence = 95.0

        else:
            # ==================================
            # ML-BASED DECISION
            # ==================================
            input_features = np.array(features).reshape(1, -1)
            proba_good = model.predict_proba(input_features)[0][1]

            if proba_good >= 0.7:
                result = "Good"
            else:
                result = "Bad"

            confidence = round(proba_good * 100, 2)

        return render_template(
            "output.html",
            result=result,
            confidence=confidence
        )

    except Exception as e:
        return render_template(
            "output.html",
            result="Error",
            confidence=str(e)
        )


# ================================
# App Entry Point
# ================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2000))
    app.run(host="0.0.0.0", port=port, debug=False)
