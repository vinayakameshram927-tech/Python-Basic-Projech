import pandas as pd
import joblib as jl
import streamlit as st

# Load the trained model, scaler, and encoded columns
model_pt = jl.load("./pkl_files/heart_model.pkl")
# Loading the recreated correct StandardScaler object
scaler = jl.load("./pkl_files/real_scaler.pkl")
encoded_columns = jl.load("./pkl_files/columns.pkl")
# Remove target column if it exists in the saved columns list
if 'HeartDisease' in encoded_columns:
    encoded_columns = encoded_columns.drop('HeartDisease')

st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)

st.title("Heart Disease Prediction")
st.write("Enter the patient details below to predict the likelihood of heart disease.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=40)
resting_bp = st.number_input("Resting Blood Pressure", min_value=0, max_value=300, value=120)
cholesterol = st.number_input("Cholesterol", min_value=0, max_value=600, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
oldpeak = st.number_input("Oldpeak", min_value=-5.0, max_value=10.0, value=0.0)

sex = st.selectbox("Sex", ["M", "F"])
chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
exercise_angina = st.selectbox("Exercise Angina", ["N", "Y"])
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict Heart Disease"):
    # Create a DataFrame with a single row
    input_data = pd.DataFrame(
        {
            "S": [age],
            "RestingBP": [resting_bp],
            "Cholesterol": [cholesterol],
            "FastingBS": [fasting_bs],
            "MaxHR": [max_hr],
            "Oldpeak": [oldpeak],
            "Sex": [sex],
            "ChestPainType": [chest_pain_type],
            "RestingECG": [resting_ecg],
            "ExerciseAngina": [exercise_angina],
            "ST_Slope": [st_slope]
        })
    
    # get_dummies without drop_first=True to match notebook training
    input_data = pd.get_dummies(input_data)
    
    # Ensure all expected columns are present
    input_df = input_data.reindex(columns=encoded_columns, fill_value=0)
 
    # Scale the input
    input_scaled = scaler.transform(input_df)
    
    # Predict the outcome
    prediction = model_pt.predict(input_scaled)
    
    if prediction[0] == 1:
        st.error("Prediction: The patient is likely to have heart disease.")
    else:
        st.success("Prediction: The patient is unlikely to have heart disease.")
