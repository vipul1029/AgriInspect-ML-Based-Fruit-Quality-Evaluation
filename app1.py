# # # # Import Libraries
# # # import os
# # # import numpy as np
# # # import pickle
# # # from flask import Flask, request, render_template

# # # # Flask App Initialization
# # # app = Flask(
# # #     __name__,
# # #     template_folder="templates",
# # #     static_folder="static"
# # # )

# # # # Load ML Model
# # # MODEL_PATH = "best.pkl"

# # # with open(MODEL_PATH, "rb") as file:
# # #     model = pickle.load(file)

# # # # Routes
# # # @app.route("/")
# # # def home():
# # #     return render_template("index.html")

# # # @app.route("/predict", methods=["GET", "POST"])
# # # def predict():
# # #     return render_template("inner-page.html")

# # # @app.route("/submit", methods=["POST"])
# # # def submit():
# # #     # Read form inputs
# # #     input_features = [int(float(x)) for x in request.form.values()]
# # #     input_features = np.array([input_features])

# # #     # Prediction
# # #     prediction = model.predict(input_features)[0]

# # #     result = "Good" if int(prediction) == 1 else "Bad"

# # #     return render_template("output.html", result=result)

# # # # Render Deployment Entry Point
# # # if __name__ == "__main__":
# # #     port = int(os.environ.get("PORT", 2000))
# # #     app.run(host="0.0.0.0", port=port)







# # # ================================
# # # Import Libraries
# # # ================================
# # import os
# # import numpy as np
# # import xgboost as xgb
# # from flask import Flask, request, render_template

# # # ================================
# # # Flask App Initialization
# # # ================================
# # app = Flask(
# #     __name__,
# #     template_folder="templates",
# #     static_folder="static"
# # )

# # # ================================
# # # Load XGBoost Model (CORRECT WAY)
# # # ================================
# # MODEL_PATH = "best.pkl"

# # model = xgb.Booster()
# # model.load_model(MODEL_PATH)

# # # ================================
# # # Routes
# # # ================================
# # @app.route("/")
# # def home():
# #     return render_template("index.html")


# # @app.route("/predict", methods=["GET", "POST"])
# # def predict():
# #     return render_template("inner-page.html")


# # @app.route("/submit", methods=["POST"])
# # def submit():
# #     try:
# #         # Read form inputs
# #         input_features = [float(x) for x in request.form.values()]
# #         input_features = np.array(input_features).reshape(1, -1)

# #         # Convert to DMatrix (REQUIRED for Booster)
# #         dmatrix = xgb.DMatrix(input_features)

# #         # Prediction
# #         prediction = model.predict(dmatrix)[0]

# #         # Result
# #         result = "Good" if int(prediction) == 1 else "Bad"

# #         return render_template("output.html", result=result)

# #     except Exception as e:
# #         return render_template("output.html", result=f"Error: {str(e)}")


# # # ================================
# # # App Entry Point
# # # ================================
# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 2000))
# #     app.run(host="0.0.0.0", port=port, debug=True)






# # ================================
# # Import Libraries
# # ================================
# import os
# import numpy as np
# from flask import Flask, request, render_template
# from xgboost import XGBClassifier

# # ================================
# # Flask App Initialization
# # ================================
# app = Flask(
#     __name__,
#     template_folder="templates",
#     static_folder="static"
# )

# # ================================
# # Load XGBoost Model (SKLEARN API)
# # ================================
# MODEL_PATH = "best.pkl"

# model = XGBClassifier()
# model.load_model(MODEL_PATH)

# # ================================
# # Routes
# # ================================
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     return render_template("inner-page.html")


# @app.route("/submit", methods=["POST"])
# def submit():
#     try:
#         # Read inputs
#         input_features = [float(x) for x in request.form.values()]
#         input_features = np.array(input_features).reshape(1, -1)

#         # Predict
#         prediction = model.predict(input_features)[0]

#         result = "Good" if int(prediction) == 1 else "Bad"

#         return render_template("output.html", result=result)

#     except Exception as e:
#         return render_template("output.html", result=f"Error: {str(e)}")


# # ================================
# # App Entry Point
# # ================================
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 2000))
#     app.run(host="0.0.0.0", port=port, debug=True)








# # ================================
# # Import Libraries
# # ================================
# import os
# import numpy as np
# from flask import Flask, request, render_template
# from xgboost import XGBClassifier

# # ================================
# # Flask App Initialization
# # ================================
# app = Flask(
#     __name__,
#     template_folder="templates",
#     static_folder="static"
# )

# # ================================
# # Load XGBoost Model (CORRECT FILE)
# # ================================
# MODEL_PATH = "best.json"   # ✅ MUST be best.json

# model = XGBClassifier()
# model.load_model(MODEL_PATH)

# # ================================
# # Routes
# # ================================
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     return render_template("inner-page.html")


# @app.route("/submit", methods=["POST"])
# def submit():
#     try:
#         # Read inputs
#         input_features = [float(x) for x in request.form.values()]
#         input_features = np.array(input_features).reshape(1, -1)

#         # Predict
#         prediction = model.predict(input_features)[0]

#         result = "Good" if int(prediction) == 1 else "Bad"

#         return render_template("output.html", result=result)

#     except Exception as e:
#         return render_template("output.html", result=f"Error: {str(e)}")


# # ================================
# # App Entry Point
# # ================================
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 2000))
#     app.run(host="0.0.0.0", port=port, debug=False)







# # ================================
# # Import Libraries
# # ================================
# import os
# import numpy as np
# from flask import Flask, request, render_template
# from xgboost import XGBClassifier

# # ================================
# # Flask App Initialization
# # ================================
# app = Flask(
#     __name__,
#     template_folder="templates",
#     static_folder="static"
# )

# # ================================
# # Load Trained XGBoost Model
# # ================================
# MODEL_PATH = "best.json"   # MUST be best.json

# model = XGBClassifier()
# model.load_model(MODEL_PATH)

# # ================================
# # Routes
# # ================================
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     return render_template("inner-page.html")


# @app.route("/submit", methods=["POST"])
# def submit():
#     try:
#         # Read input values from form
#         input_features = [float(x) for x in request.form.values()]
#         input_features = np.array(input_features).reshape(1, -1)

#         # Get probability of GOOD class
#         proba_good = model.predict_proba(input_features)[0][1]

#         # STRICT decision threshold
#         if proba_good >= 0.7:
#             result = "Good"
#         else:
#             result = "Bad"

#         confidence = round(proba_good * 100, 2)

#         return render_template(
#             "output.html",
#             result=result,
#             confidence=confidence
#         )

#     except Exception as e:
#         return render_template(
#             "output.html",
#             result="Error",
#             confidence=str(e)
#         )


# # ================================
# # App Entry Point
# # ================================
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 2000))
#     app.run(host="0.0.0.0", port=port, debug=False)




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
