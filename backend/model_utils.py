import joblib
import pandas as pd

MODEL_PATH = "../models/loan_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict(data: dict):
    model = load_model()

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    return str(prediction)
