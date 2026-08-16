# Week 05 — Model Deployment

## Customer Churn Prediction Web App

This project deploys a trained Machine Learning model as an interactive
web application using Streamlit.

The customer churn prediction pipeline was trained using Scikit-learn
and saved with Joblib. The saved pipeline is loaded by the Streamlit
application to make predictions on new customer information.

## Objective

The objective of this task is to convert a trained Machine Learning model
into a simple, shareable, and usable web application.

Users can enter customer information through the web interface and
receive a prediction showing whether the customer is likely to churn.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Machine Learning Model

The application uses the final Logistic Regression pipeline developed
during the Week 04 Machine Learning Pipeline task.

The pipeline includes:

- Numerical feature preprocessing
- StandardScaler
- Categorical feature preprocessing
- OneHotEncoder
- Logistic Regression

The complete trained pipeline was saved as:

`final_churn_pipeline.joblib`

Saving the complete pipeline ensures that the same preprocessing steps
used during training are automatically applied when making predictions
in the web application.

## Streamlit Application

The Streamlit application provides input fields for customer information,
including:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Streaming Services
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

After entering the customer information, the user can click the
**Predict Churn** button.

The application then displays whether the customer is likely to churn.

## Live Application

🚀 **Try the deployed application:**

https://customer-churn-prediction-neurofive.streamlit.app/

The application is deployed using **Streamlit Community Cloud** and is
available online for testing.

## Project Structure

```text
Week-05-Model-Deployment/
│
├── app.py
├── final_churn_pipeline.joblib
├── requirements.txt
└── README.md