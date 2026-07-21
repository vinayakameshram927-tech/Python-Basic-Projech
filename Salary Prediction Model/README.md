```markdown
# Salary Prediction Project

## Project Description
This project aims to predict salaries based on various features such as age, gender, education level, job title, and years of experience. The process involves data cleaning, exploratory data analysis, feature engineering (one-hot encoding and scaling), and training a linear regression model.

## Data Source
The data used in this project is sourced from `Salary_Data.csv`. It contains information about individuals' demographics, education, job roles, and their corresponding salaries.

## Model Used
A `Linear Regression` model from `scikit-learn` was used for salary prediction. The model was trained on scaled features and achieved an R-squared score of approximately `0.85`.

## Files
* `Salary_Data.csv`: The raw dataset.
* `LR_Salary.pkl`: The trained Linear Regression model.
* `scaled_x.pkl`: The StandardScaler object used for scaling the features.
* `columns.pkl`: The list of columns after one-hot encoding, used for consistent feature ordering during prediction.

## Frontend Integration with Streamlit
To create a frontend using Streamlit, you will need to load the saved model, scaler, and column information. Below are the steps and example code snippets:

### 1. Install necessary libraries
```bash
pip install streamlit pandas scikit-learn joblib
```