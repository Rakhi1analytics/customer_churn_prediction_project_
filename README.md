# customer_churn_prediction_project_
## Customer Churn Prediction
This project aims to predict customer churn in a telecom company using machine learning techniques. It includes Exploratory Data Analysis (EDA), feature engineering, model building, evaluation, and deployment through a Streamlit web app.
## Problem Statement
Customer churn is when customers stop doing business with a company. Identifying customers likely to churn can help businesses take proactive measures to retain them. This project uses telecom customer data to build a predictive model.
## Project Workflow
•	Data Cleaning:
- Removed missing values and duplicates
- Converted categorical features
- Addressed class imbalance using SMOTE
•	Exploratory Data Analysis (EDA):
- Analyzed churn trends by gender, contract type, internet usage, etc.
- Used bar plots, pie charts, and count plots for insights
•	Feature Engineering:
- Encoded categorical variables
- Scaled numerical features using StandardScaler
•	Model Building:
- Trained multiple models: Logistic Regression, Decision Tree, etc.
- Evaluated using Accuracy, Precision, Recall, F1-Score
•	Model Deployment:
- Best model saved using joblib
- Deployed using a clean Streamlit app
## Algorithms Used
•	Logistic Regression
•	Decision Tree Classifier
•	Random Forest (optional)
•	SMOTE (for handling imbalance)
 Streamlit Web App
You can launch the app locally with:
streamlit run app.py
## App Features:
- Interactive dashboard with churn insights
- Predicts churn based on customer inputs
- Clean, responsive UI
## Project Structure

Customer-Churn-Prediction/
│
├── app.py                 # Streamlit application
├── churn_model.pkl        # Trained ML model
├── customer_data.csv      # Sample dataset
├──notebook                        
├── README.md              # Project documentation

## Key Insights
•	Customers with month-to-month contracts are more likely to churn.
•	Fiber optic internet users show higher churn rates.
•	Paperless billing and electronic payment methods correlate with higher churn.
## Dataset
Source: Telco Customer Churn Dataset (Kaggle)
Size: ~7,000 records
## Author
Rakhi Chahar
Final-year student | Aspiring Data Analyst
## Future Improvements
•	Hyperparameter tuning with GridSearchCV
•	Add more models like XGBoost or CatBoost
•	Deploy online using Streamlit Cloud
