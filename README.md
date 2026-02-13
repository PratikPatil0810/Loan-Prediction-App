# Loan Prediction System

## Overview

This project is a simple Loan Prediction web application.

It has: - FastAPI backend for model prediction - Streamlit frontend for
user interaction - Machine Learning model to predict loan approval

## Features

-   Upload training dataset
-   Upload testing dataset
-   Enter single user details for prediction
-   View model accuracy and evaluation metrics
-   See clear prediction result

## How to Run the Project

### Step 1: Install Requirements

Open terminal and run: pip install -r requirements.txt

### Step 2: Start Backend Server

Run: uvicorn main:app --reload

Backend will run at: http://127.0.0.1:8000

### Step 3: Start Frontend

Open a new terminal and run: streamlit run app.py

Frontend will run at: http://localhost:8501

## API Endpoints

-   /train - Train model
-   /predict - Predict loan status
-   /metrics - Get accuracy and evaluation

## Tech Stack

-   Python
-   FastAPI
-   Streamlit
-   Scikit-learn
