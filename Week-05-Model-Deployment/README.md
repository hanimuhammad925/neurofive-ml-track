# Week 05 — Model Deployment

## Customer Churn Prediction Web App

This project converts a trained machine learning model into a simple
interactive web application using Streamlit.

The trained customer churn prediction pipeline was saved using Joblib
and integrated into a Streamlit application.

## Project Objective

The objective of this task is to deploy a machine learning model so that
users can provide customer information and receive a churn prediction
through a web interface.

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Streamlit

## Machine Learning Model

The application uses the final Logistic Regression pipeline developed
during the Week 04 ML Pipeline task.

The complete pipeline includes:

- Numerical feature preprocessing
- StandardScaler
- Categorical feature encoding
- OneHotEncoder
- Logistic Regression

The complete trained pipeline was saved as:

`final_churn_pipeline.joblib`

This allows the application to perform the same preprocessing and
prediction steps on new customer data.

## Streamlit Application

The application provides input fields for customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract
- Payment Method
- Monthly Charges
- Total Charges
- Other customer service information

After entering the customer information, the user can click the
**Predict Churn** button.

The application then displays whether the customer is likely to churn.

## Live Application

[Open the Live Customer Churn Prediction App](https://customer-churn-prediction-neurofive.streamlit.app/)

## Project Files

```text
Week-05-Model-Deployment/
│
├── app.py
├── final_churn_pipeline.joblib
├── requirements.txt
└── README.md