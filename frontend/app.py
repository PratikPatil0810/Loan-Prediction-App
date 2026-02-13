import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Loan Prediction System", layout="wide")

st.title("Loan Approval Prediction System")

menu = st.sidebar.radio(
    "Navigation",
    ["Train Model", "Test Model", "Predict Loan"]
)


if menu == "Train Model":

    st.header("Upload Training Dataset")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if st.button("Train Model"):

        if file is not None:
            files = {"file": file.getvalue()}
            response = requests.post(f"{API}/train", files=files)
            data = response.json()
            st.success(data["message"])
            st.write(f"Training Accuracy: {round(data['accuracy']*100,2)}%")
            
        else:
            st.error("Please upload dataset")



elif menu == "Test Model":

    st.header("Upload Test Dataset")

    file = st.file_uploader("Upload CSV file", type=["csv"])

    if st.button("Evaluate Model"):

        if file is not None:
            files = {"file": file.getvalue()}
            response = requests.post(f"{API}/test", files=files)

            if response.status_code == 200:
                data = response.json()

                st.success("Predictions generated successfully!")

                preds = data["predictions"]

                st.write("###Predictions:")
                st.write(preds)

            else:
                st.error("Backend Error:")
                st.code(response.text)

        else:
            st.error("Please upload dataset")



else:

    st.header("Enter Applicant Details")

    col1, col2 = st.columns(2)

    with col1:
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Married = st.selectbox("Married", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

    with col2:
        ApplicantIncome = st.number_input("Applicant Income", 0)
        CoapplicantIncome = st.number_input("Coapplicant Income", 0)
        LoanAmount = st.number_input("Loan Amount", 0)
        Loan_Amount_Term = st.number_input("Loan Term", 0)
        Credit_History = st.selectbox("Credit History", [0, 1])
        Property_Area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    st.divider()

    if st.button("Predict Loan Approval", use_container_width=True):

        data = {
            "Gender": Gender,
            "Married": Married,
            "Dependents": Dependents,
            "Education": Education,
            "Self_Employed": Self_Employed,
            "ApplicantIncome": ApplicantIncome,
            "CoapplicantIncome": CoapplicantIncome,
            "LoanAmount": LoanAmount,
            "Loan_Amount_Term": Loan_Amount_Term,
            "Credit_History": Credit_History,
            "Property_Area": Property_Area,
        }

        response = requests.post(f"{API}/predict", json=data)

        prediction = response.json()["prediction"]

        st.divider()

        if prediction == "Y":
            st.success("Loan Approved")
        else:
            st.error("Loan Not Approved")
