import pandas as pd
import joblib as jl
import streamlit as st

# Pandas library is used to create a data frame 
# Joblib library is used to create a pkl files of created model which is used to implement on frontend
# Streamlit library is used to create frontend where we can implement our ML model

model_pt = jl.load("./pkl_files/LR_ford_car.pkl")
scaler = jl.load("./pkl_files/scaler.pkl")
encoded_columns = jl.load("./pkl_files/columns.pkl")

st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout = "centered"
)
st.title("Ford Car Predicton")
st.write("Enter the car details below to predict its selling price.")

year = st.number_input(
    "Manifacturing Year",
    min_value = 1996,
    max_value = 2026,
    value = 2018
)

mileage = st.number_input(
    "mileage",
    min_value = 1,
    max_value = 177644,
    value = 5000
)

tax = st.number_input(
    "Road Tax",
    min_value = 0,
    max_value = 580,
    value = 100
)

mpg = st.number_input(
    "MPG",
    min_value = 20,
    max_value = 201,
    value = 70
)

engineSize = st.number_input(
    "Engine Size",
    min_value = 0,
    max_value = 5,
    value = 3
)

transmission = st.selectbox(
    "Transmission",
    [
        "Automatic",
        "Manual",
        "Semi-Auto"
    ]
)

fuelType = st.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "Hybrid",
        "Electric",
        "Other"
    ]
)
model = st.text_input("Model",value="Focus")

if st.button("Predict Price"):
    # Create a DataFrame with a single row of zeros for all expected columns
    input_data = pd.DataFrame(
        {
            "year": [year],
            "model": [model],
            "transmission": [transmission],
            "mileage": [mileage],
            "fuelType": [fuelType],
            "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize]
        })
    
    input_data = pd.get_dummies(input_data,columns = ["model","transmission","fuelType"],drop_first=True)
    input_df = input_data.reindex(columns=encoded_columns, fill_value=0)
 
    # Scale the input
    input_scaled = scaler.transform(input_df)
    
    # Predict the price
    prediction = model_pt.predict(input_scaled)
    
    st.success("The predicted selling price is: £ " + str(round(prediction[0])))
