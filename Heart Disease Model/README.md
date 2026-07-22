
# Heart Disease Prediction Project

## Project Overview

This notebook demonstrates an end-to-end machine learning pipeline for predicting heart disease using a dataset containing various health-related features.

### Data Source
The dataset used in this analysis is `heart.csv`, uploaded from the local system.

### Notebook Steps
1.  **Load Data**: The `heart.csv` dataset is loaded into a pandas DataFrame.
2.  **Initial Data Exploration**: Basic checks are performed, including displaying the head, shape, info, null values, and duplicates.
3.  **Data Cleaning**:
    *   Identified and handled zero values in 'Cholesterol' and 'RestingBP' by replacing them with the mean of their respective non-zero values.
4.  **Feature Engineering**: Categorical features are one-hot encoded using `pd.get_dummies`.
5.  **Data Scaling**: Numerical features are scaled using `StandardScaler`.
6.  **Model Training**: A Logistic Regression model is trained on the preprocessed data.
7.  **Model Evaluation**: The model's performance is evaluated using a confusion matrix and classification report.
8.  **Model Export**: The trained model, scaler, and column names are saved using `joblib` for future deployment.
