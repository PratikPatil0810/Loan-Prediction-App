from fastapi import FastAPI, UploadFile, File
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import joblib
from model_utils import predict, load_model

app = FastAPI()

MODEL_PATH = "../models/loan_model.pkl"


@app.get("/")
def home():
    return {"message": "Loan Prediction API Running"}



@app.post("/train")
async def train_model(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
    df['LoanAmount_log'] = np.log(df['LoanAmount'])
    df.drop(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount'], axis=1, inplace=True)

    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = load_model()
    model.fit(X_train, y_train)
    preds = model.predict(X_val)

    accuracy = accuracy_score(y_val, preds)

    return {
    "message": "Model trained successfully",
    "accuracy": float(accuracy)
}


@app.post("/test")
async def test_model(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
    df['LoanAmount_log'] = np.log(df['LoanAmount'])
    df.drop(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount'], axis=1, inplace=True)

    X = df.copy()

    model = load_model()

    preds = model.predict(X)

    return {"predictions": preds.tolist()}


@app.post("/predict")
async def predict_loan(data: dict):
    df = pd.DataFrame([data])

    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
    df["LoanAmount_log"] = np.log(df["LoanAmount"])
    df.drop(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount'], axis=1, inplace=True)

    model = load_model()

    prediction = model.predict(df)[0]

    return {"prediction": str(prediction)}
