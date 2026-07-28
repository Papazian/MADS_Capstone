import streamlit as st
import pandas as pd
import pickle

# 1. Load the trained model
@st.cache_resource
def load_model():
    # Replace with your actual saved model file path
    with open("grad_boost_sklearn_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# 2. Build the app UI
st.title("Model Scoring Dashboard")
st.write("Adjust the input features below to score a new sample.")

# User inputs (modify features based on your dataset)
age = st.slider("Age", 18, 100, 30)
income = st.number_input("Income ($)", 10000, 200000, 50000)
score = st.slider("Credit Score", 300, 850, 650)

# 3. Process and score data
if st.button("Score Model"):
    # Create input DataFrame matching training feature names
    input_data = pd.DataFrame([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 1, 0, 1, 0, 0, 0, 1, 0, 0]], columns=['Product_Checking_or_savings_account', 'Product_Credit_card', 'Product_Debt_collection', 'Product_Debt_or_credit_management','Product_Money_transfer_virtual_currency_or_money_service', 'Product_Mortgage', 'Product_Payday_loan_title_loan_personal_loan_or_advance_loan','Product_Prepaid_card', 'Product_Student_loan', 'Product_Vehicle_loan_or_lease', 'Older_American', 'Servicemember', 'complaint_word_count', 'dollar_sign', 'critical_severity_keywords','high_severity_keywords', 'medium_severity_keywords', 'financial_loss_keywords', 'credit_damage_keywords', 'credit_bureau', 'credit_union', 'Southern_State'])
    
    # Run prediction / scoring
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None
    
    # Display results
    st.success(f"Prediction Result: {prediction[0]}")
    if prediction_proba is not None:
        st.write(f"Prediction Probability: {prediction_proba[0].max():.2f}")
        
