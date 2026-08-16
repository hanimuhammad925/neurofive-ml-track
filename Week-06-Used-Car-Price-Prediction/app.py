import streamlit as st
import pandas as pd
import joblib

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ==========================================
# Load Trained Model
# ==========================================

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "used_car_price_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error("Unable to load the trained model.")
    st.exception(e)
    st.stop()


# ==========================================
# Title
# ==========================================

st.title("🚗 Used Car Price Prediction")

st.write(
    "Enter the details of a used car below to estimate its market price."
)

st.divider()


# ==========================================
# Input Section
# ==========================================

st.subheader("🚘 Car Information")


name = st.text_input(
    "Car Name",
    value="Maruti Swift"
)


location = st.selectbox(
    "Location",
    [
        "Mumbai",
        "Pune",
        "Chennai",
        "Coimbatore",
        "Hyderabad",
        "Jaipur",
        "Kochi",
        "Kolkata",
        "Delhi",
        "Bangalore",
        "Ahmedabad"
    ]
)


year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2026,
    value=2018,
    step=1
)


kilometers_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=1000000,
    value=50000,
    step=1000
)


fuel_type = st.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "CNG",
        "LPG",
        "Electric"
    ]
)


transmission = st.selectbox(
    "Transmission",
    [
        "Manual",
        "Automatic"
    ]
)


owner_type = st.selectbox(
    "Owner Type",
    [
        "First",
        "Second",
        "Third",
        "Fourth & Above"
    ]
)


# ==========================================
# Numeric Features
# ==========================================

mileage = st.number_input(
    "Mileage",
    min_value=1.0,
    max_value=50.0,
    value=18.0,
    step=0.1
)


engine = st.number_input(
    "Engine (CC)",
    min_value=500.0,
    max_value=8000.0,
    value=1200.0,
    step=50.0
)


power = st.number_input(
    "Power (bhp)",
    min_value=20.0,
    max_value=1000.0,
    value=80.0,
    step=1.0
)


seats = st.number_input(
    "Number of Seats",
    min_value=2.0,
    max_value=10.0,
    value=5.0,
    step=1.0
)


new_price = st.number_input(
    "New Price (Lakh)",
    min_value=0.0,
    max_value=500.0,
    value=10.0,
    step=0.1
)


st.divider()


# ==========================================
# Prediction
# ==========================================

if st.button(
    "🔮 Predict Car Price",
    use_container_width=True
):

    # --------------------------------------
    # Create input DataFrame
    # --------------------------------------

    input_data = pd.DataFrame({
        "Name": [name],
        "Location": [location],
        "Year": [year],
        "Kilometers_Driven": [kilometers_driven],
        "Fuel_Type": [fuel_type],
        "Transmission": [transmission],
        "Owner_Type": [owner_type],

        # IMPORTANT:
        # These are numeric because the trained
        # model expects numeric values.
        "Mileage": [mileage],
        "Engine": [engine],
        "Power": [power],
        "Seats": [seats],
        "New_Price": [new_price]
    })


    # ======================================
    # Feature Engineering
    # ======================================

    # Car age
    input_data["Car_Age"] = (
        2026 - input_data["Year"]
    )


    # Extract brand from car name
    input_data["Brand"] = (
        input_data["Name"]
        .str.split()
        .str[0]
    )


    # ======================================
    # Make Prediction
    # ======================================

    try:

        prediction = model.predict(
            input_data
        )[0]


        # ==================================
        # Display Prediction
        # ==================================

        st.success(
            f"💰 Estimated Car Price: ₹ {prediction:.2f} Lakh"
        )


        st.info(
            "The prediction is generated using "
            "the trained Random Forest model."
        )


        # ----------------------------------
        # Show Input Details
        # ----------------------------------

        with st.expander("View Input Details"):

            st.dataframe(
                input_data,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.exception(e)