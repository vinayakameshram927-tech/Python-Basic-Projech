## README.md (Streamlit Frontend)

# Ford Car Price Prediction Streamlit App

## Overview
This Streamlit application provides an interactive frontend for the Ford Car Price Prediction model. Users can input various car features (model, year, transmission, mileage, fuel type, tax, MPG, and engine size) and receive an instant predicted price for the car.

## Features
-   **Interactive Input Fields**: Easy-to-use widgets for entering car specifications.
-   **Real-time Prediction**: Get price predictions immediately after entering details.
-   **Model Integration**: Seamlessly loads and utilizes the pre-trained Linear Regression model and data preprocessors.

## Prerequisites
To run this application, you need Python and the following libraries installed:
-   `streamlit`
-   `pandas`
-   `scikit-learn` (specifically for `StandardScaler` and `LinearRegression` during model loading)
-   `joblib`

Install them using pip:
```bash
pip install streamlit pandas scikit-learn joblib
```

## Setup
1.  **Download the project files**: Ensure you have `app.py`, `LR_ford_car.pkl`, `scaler.pkl`, and `columns.pkl` in the same directory.
    -   `app.py`: The Streamlit application code.
    -   `LR_ford_car.pkl`: The trained Linear Regression model.
    -   `scaler.pkl`: The fitted `StandardScaler` object used for numerical feature scaling.
    -   `columns.pkl`: A list of column names used during training, essential for consistent one-hot encoding.

2.  **Ensure model artifacts are present**: The `app.py` script expects the model, scaler, and column list to be available as `.pkl` files in the same directory.

## Usage
To launch the Streamlit application, navigate to the directory containing `app.py` in your terminal and run:

```bash
streamlit run app.py
```

This command will open a new tab in your web browser with the Streamlit application. If running in a cloud environment like Google Colab, it will provide a public URL for access.

## How it Works
1.  **Loads Assets**: The `app.py` script first loads the pre-trained `lr_model`, `scaler`, and `model_columns` using `joblib`.
2.  **User Input**: Streamlit widgets (`selectbox`, `slider`, `number_input`) collect car features from the user.
3.  **Data Preprocessing**: The user inputs are transformed into a pandas DataFrame. Categorical features are one-hot encoded (ensuring consistency with training data columns), and numerical features are scaled using the loaded `scaler`.
4.  **Prediction**: The preprocessed input is fed into the loaded `lr_model` to generate a price prediction.
5.  **Display Result**: The predicted car price is displayed to the user.