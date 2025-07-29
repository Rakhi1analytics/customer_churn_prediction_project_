import streamlit as st
import pandas as pd
import joblib

# Load model and column structure
model = joblib.load("C:/Users/DELL/final_churn_model.pkl")
columns = joblib.load("C:/Users/DELL/churn_columns.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("🔍 Customer Churn Prediction App")
st.markdown("Upload customer details to predict whether they are likely to churn.")

# Sidebar input
st.sidebar.header("Input Customer Information")

def user_input_features():
    
    input_data = {}
    for col in columns:
        if "yes" in col.lower() or "no" in col.lower() or col in ["SeniorCitizen", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]:
            input_data[col] = st.sidebar.selectbox(f"{col}:", ["Yes", "No"])
        elif col == "gender":
            input_data[col] = st.sidebar.selectbox("Gender", ["Male", "Female"])
        elif "Charges" in col or "Monthly" in col or "Total" in col:
            input_data[col] = st.sidebar.number_input(f"{col}:", min_value=0.0, step=1.0)
        elif col == "tenure":
            input_data[col] = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
        else:
            input_data[col] = st.sidebar.text_input(f"{col}:")
    return pd.DataFrame([input_data])

# Collect user input
input_df = user_input_features()

# Convert known categorical fields to numeric
input_df = input_df.replace({
    "Yes": 1,
    "No": 0,
    "Male": 1,
    "Female": 0
})

# Ensure DataFrame has same structure as training data
input_df = input_df.reindex(columns=columns, fill_value=0)

# Replace empty strings with 0
input_df = input_df.replace('', 0)

# Convert all columns to numeric if possible (fill NaN with 0)
for col in input_df.columns:
    input_df[col] = pd.to_numeric(input_df[col], errors='coerce').fillna(0)

# Display user input
st.subheader("Customer Input Details")
st.write(input_df)

# Predict and display result
if st.button("Predict Churn"):
    try:
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1]

        if prediction == 1:
            st.error(f"⚠️ This customer is likely to churn! (Probability: {proba:.2f})")
        else:
            st.success(f"✅ This customer is likely to stay. (Probability: {proba:.2f})")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
