import pandas as pd
import joblib as jl
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Pandas library is used to create a data frame 
# Joblib library is used to create a pkl files of created model which is used to implement on frontend
# Streamlit library is used to create frontend where we can implement our ML model

# Load the trained model and encoded columns
model_pt = jl.load("./pkl_files/LR_Salary.pkl")
encoded_columns = jl.load("./pkl_files/columns.pkl")

# Load the scaler
scaler = jl.load("./pkl_files/scaler.pkl")

st.set_page_config(
    page_title="Salary Predictor",
    layout = "centered"
)
# Above code is used to set the page title and layout of the streamlit app 

st.title("Salary Prediction")
st.write("Enter the employee details below to predict their salary.")

age = st.number_input(
    "Age",
    min_value = 18,
    max_value = 100,
    value = 30
)
years_of_experience = st.number_input(
    "Years of Experience",
    min_value = 0.0,
    max_value = 60.0,
    value = 5.0
)
gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)
education_level = st.selectbox(
    "Education Level",
    [
        "Bachelor's",
        "Master's",
        "PhD"
    ]
)

job_title = st.text_input("Job Title", value="Software Engineer")

if st.button("Predict Salary"):
    # Create a DataFrame with a single row for all expected inputs
    input_data = pd.DataFrame(
        {
            "Age": [age],
            "Gender": [gender],
            "Education Level": [education_level],
            "Job Title": [job_title],
            "Years of Experience": [years_of_experience]
        })
    
    input_data = pd.get_dummies(input_data, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
    input_df = input_data.reindex(columns=encoded_columns, fill_value=0)
 
    # Scale the input
    input_scaled = scaler.transform(input_df)
    
    # Predict the salary
    prediction = model_pt.predict(input_scaled)
    
    st.success("The predicted salary is: Rs. " + str(round(prediction[0])))
