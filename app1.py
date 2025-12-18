# Import Libraries
import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')
# Add File Path for Model
pickle_file_path = "best.pkl"

with open(pickle_file_path, 'rb') as file:
    try:
        model = pickle.load(file)
    except ValueError as e:
        if "itemsize" in str(e):
            # Handle incompatible dtype
            msg = "Incompatible dtype issue in the node array."
            raise ValueError(msg)
        else:
            raise e

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST", "GET"])
def predict():
    return render_template("inner-page.html")

@app.route('/submit', methods=["POST", "GET"])
def submit():
    # Read inputs
    input_feature = [int(float(x)) for x in request.form.values()]
    input_feature = [np.array(input_feature)]

    # Make Predictions
    print(type(model))
    prediction = model.predict(input_feature)
    prediction = int(prediction)

    if prediction == 0:
        return render_template("output.html", result="Bad")
    else:
        return render_template("output.html", result="Good")

if __name__ == "__main__":
    app.run(debug=True, port=2000)
