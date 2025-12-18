# 🍏 AgriInspect – ML-Based Fruit Quality Evaluation

AgriInspect is a machine learning–based web application that helps predict **fruit quality** using key attributes.  
The goal of this project is to understand how machine learning models can be used in real-world agricultural applications and how they can be integrated into a simple web app.


---

## 🌱 Why I built this project

In many agricultural and supply-chain processes, fruit quality checking is still done manually.  
This can be time-consuming and inconsistent.

With **AgriInspect**, I wanted to:
- Explore how ML can help in quality assessment
- Learn how to load and use a trained model
- Build a simple Flask web interface for predictions
- Understand real-world issues like dependencies and deployment

---

## 🧠 What this project does

- Takes fruit-related input values from the user
- Uses a trained machine learning model to analyze the data
- Predicts the quality of the fruit
- Displays the result instantly on a web page

---

## 🛠️ Tech Stack Used

- **Python**
- **Flask**
- **NumPy & Pandas**
- **Scikit-learn**
- **XGBoost**
- **HTML & CSS**

---

## 📂 Project Structure

AgriInspect-ML-Based-Fruit-Quality-Evaluation/
├── app1.py # Flask application
├── best.pkl # Trained ML model
├── apple_quality.csv # Dataset
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── static/ # Images & assets
│ ├── assets/
│ ├── screenshots/
│ └── demonstration/
└── templates/ # HTML templates
├── index.html
├── output.html
└── inner-page.html


---

## 🔍 Model Information

- The ML model is already trained and saved as `best.pkl`
- Uses **XGBoost** for prediction
- Loaded at runtime using Python’s `pickle` module


---

## 🚀 What I Learned From This Project

- Integrating ML models with Flask
- Handling dependency and environment issues
- Using `requirements.txt` for reproducibility
- Debugging real-world ML deployment problems
- Writing clean and structured project documentation

---

## 🌱 Future Improvements

- Support for multiple fruit types
- Better UI design
- REST API version using FastAPI
- Cloud deployment
- Model retraining pipeline

---


## 👨‍💻 Author

**Vipul Kumar**  
B.Tech CSE, VIT Vellore 
