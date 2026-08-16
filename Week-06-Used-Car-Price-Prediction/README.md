# 🚗 Used Car Price Prediction

An end-to-end machine learning project that predicts the resale price of
a used car and provides the prediction through an interactive Streamlit
application.

## Problem Statement

Used-car prices depend on factors such as manufacturing year, kilometers
driven, fuel type, transmission, engine, power, mileage, brand,
location, and ownership history. This project builds a regression model
to estimate a car's resale price in Indian Lakh (₹).

## Project Workflow

**Problem Definition → Data Cleaning → EDA → Feature Engineering →
Multiple Models → Evaluation → Best Model Selection → Model Saving →
Streamlit Deployment**

## Dataset

The project uses two CSV files:

-   `train-data.csv` --- 6,019 rows and 14 columns, including the target
    `Price`.
-   `test-data.csv` --- 1,234 rows and 13 columns, without the target.

Important features include `Name`, `Location`, `Year`,
`Kilometers_Driven`, `Fuel_Type`, `Transmission`, `Owner_Type`,
`Mileage`, `Engine`, `Power`, `Seats`, and `New_Price`.

## Data Cleaning

Several fields contained units as text, such as `18.5 kmpl`, `1197 CC`,
`82.85 bhp`, and `8.61 Lakh`. These were converted into usable numerical
values. Missing values were handled during preprocessing, and the
index-like `Unnamed: 0` column was excluded from meaningful modelling.

## Feature Engineering

Two additional features were created:

-   **Car_Age** --- calculated from the manufacturing year.
-   **Brand** --- extracted from the first word of the car name.

## Exploratory Data Analysis

The strongest numerical relationships with `Price` included:

-   Power: approximately **0.77 correlation**
-   Engine: approximately **0.66 correlation**
-   Year: approximately **0.31 correlation**
-   Mileage: approximately **-0.31 correlation**

This indicates that vehicle specifications, especially power and engine
capacity, are important price-related factors.

## Models Compared

Three regression models were trained:

1.  Linear Regression
2.  Random Forest Regressor
3.  Gradient Boosting Regressor

Evaluation metrics:

-   MAE --- lower is better
-   RMSE --- lower is better
-   R² --- higher is better

## Results

  Model                        MAE         RMSE           R²
  ------------------- ------------ ------------ ------------
  **Random Forest**     **1.4791**   **3.6007**   **0.8946**
  Gradient Boosting         1.7484       3.7827       0.8837
  Linear Regression         3.1151       7.1917       0.5797

### Best Model

**Random Forest Regressor** was selected as the final model because it
achieved the strongest evaluation performance:

-   MAE: **1.4791 Lakh**
-   RMSE: **3.6007 Lakh**
-   R²: **0.8946**

The trained model is saved as:

``` text
used_car_price_model.joblib
```

## Streamlit Application

The final model is connected to a Streamlit app where users can enter
vehicle details and receive an estimated resale price.

### Live Demo

**Live URL:** Add the Streamlit Cloud URL here after deployment.

## Run Locally

Clone the repository:

``` bash
git clone https://github.com/hanimuhammad925/neurofive-ml-track.git
```

Open the Week 06 project:

``` bash
cd neurofive-ml-track/Week-06-Used-Car-Price-Prediction
```

Install dependencies:

``` bash
pip install pandas numpy scikit-learn joblib streamlit
```

Run the application:

``` bash
streamlit run app.py
```

The app will normally open at:

``` text
http://localhost:8501
```

## Project Structure

``` text
Week-06-Used-Car-Price-Prediction/
│
├── train-data.csv
├── test-data.csv
├── Used_Car_Price_Prediction.ipynb
├── used_car_price_model.joblib
├── used_car_price_predictions.csv
├── app.py
└── README.md
```

## Business / Real-World Value

A used-car price prediction system can help dealerships and individual
sellers estimate reasonable resale prices using historical data rather
than relying only on manual estimates. It can support pricing, vehicle
acquisition, and market comparison decisions.

## Future Improvements

-   Hyperparameter tuning
-   Cross-validation
-   XGBoost/LightGBM comparison
-   Better model/variant extraction from car names
-   Additional market data
-   Prediction uncertainty estimates
-   More interactive Streamlit visualizations

## Technologies

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib, Streamlit,
Jupyter Notebook, Git, and GitHub.

## Project

**Used Car Price Prediction --- Neurofive ML Track, Week 06**
