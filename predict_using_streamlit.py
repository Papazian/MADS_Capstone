import streamlit as st
import pandas as pd
import pickle
import sklearn

# Load the trained model
@st.cache_resource
def load_model(pickle_file_location):
    # Replace with your actual saved model file path
    with open(pickle_file_location, "rb") as f:
        return pickle.load(f)

# Load each trained model
logistic_reg_sklearn_model = load_model("Supervised_Learning/logistic_reg_sklearn_model.pkl")
grad_boost_sklearn_model = load_model("Supervised_Learning/grad_boost_sklearn_model.pkl")
random_forest_sklearn_model = load_model("Supervised_Learning/random_forest_sklearn_model.pkl")

# Build the app UI
st.title("MADS Capstone Project: Predicting that a Consumer Financial Complaint is Closed Respectfully")
st.write("by Alex Yoon, Po-Wen Lai, Zhou Jiang, & John Papazian")
st.write("Please provide details about your consumer financial complaint submitted to the CFPB:")

financial_product_question = st.selectbox(
    label="What type of financial product did you identified in the complaint?",
    options=['Credit reporting or other personal consumer reports', 'Checking or savings account', 'Credit card', 'Debt collection', 'Debt or credit management', 'Money transfer, virtual currency, or money service', 'Mortgage', 'Payday loan, title loan, personal loan, or advance loan', 'Prepaid card', 'Student loan', 'Vehicle loan or lease'],
    index=0
)

if (financial_product_question=='Credit reporting or other personal consumer reports'):
    Product_Credit_reporting=1
else:
    Product_Credit_reporting=0

if (financial_product_question=='Checking or savings account'):
    Product_Checking_or_savings_account=1
else:
    Product_Checking_or_savings_account=0
    
if (financial_product_question=='Credit card'):
    Product_Credit_card=1
else:
    Product_Credit_card=0
    
if (financial_product_question=='Debt collection'):
    Product_Debt_collection=1
else:
    Product_Debt_collection=0
    
if (financial_product_question=='Debt or credit management'):
    Product_Debt_or_credit_management=1
else:
    Product_Debt_or_credit_management=0
    
if (financial_product_question=='Money transfer, virtual currency, or money service'):
    Product_Money_transfer_virtual_currency=1
else:
    Product_Money_transfer_virtual_currency=0
    
if (financial_product_question=='Mortgage'):
    Product_Mortgage=1
else:
    Product_Mortgage=0
    
if (financial_product_question=='Payday loan, title loan, personal loan, or advance loan'):
    Product_Payday_loan_title_loan=1
else:
    Product_Payday_loan_title_loan=0
    
if (financial_product_question=='Prepaid card'):
    Product_Prepaid_card=1
else:
    Product_Prepaid_card=0
    
if (financial_product_question=='Student loan'):
    Product_Student_loan=1
else:
    Product_Student_loan=0
    
if (financial_product_question=='Vehicle loan or lease'):
    Product_Vehicle_loan_or_lease=1
else:
    Product_Vehicle_loan_or_lease=0

older_american_question = st.selectbox(
    label="Are you submitting a complaint by or on behalf of a consumer 62 years or older?",
    options=['False', 'True'],
    index=0
)

if (older_american_question=='False'):
    Older_American=0
else:
    Older_American=1
    
servicemember_question = st.selectbox(
    label="Are you submitting a complaint by or on behalf of a servicemember or the spouse or dependent of a servicemember?",
    options=['False', 'True'],
    index=0
)

if (servicemember_question=='False'):
    Servicemember=0
else:
    Servicemember=1
    
credit_bureau_question = st.selectbox(
    label="Are you submitting a complaint about a credit bureau?",
    options=['False', 'True'],
    index=0
)

if (credit_bureau_question=='False'):
    credit_bureau=0
else:
    credit_bureau=1

credit_union_question = st.selectbox(
    label="Are you submitting a complaint about a credit union?",
    options=['False', 'True'],
    index=0
)

if (credit_union_question=='False'):
    credit_union=0
else:
    credit_union=1

state_question = st.selectbox(
    label="Which U.S. state or territory is the complaint being filed?",
    options=['AE','AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NV','NY','OH','OK','OR','PA','PR','RI','SC','TN','TX','UT','VA','WA','WI','WV','NM','SD','WY','VI','VT','AA','AP','GU','AS','MP','PW'],
    index=23  # default to Michigan
)

Southern_States = ['AL', 'AR', 'DE', 'FL', 'GA', 'KY', 'LA', 'MD', 'MS', 'NC', 'OK', 'SC', 'TN', 'TX', 'VA', 'WV']

if (state_question in Southern_States):
    southern_state=1
else:
    southern_state=0

consumer_complaint_narrative = st.text_area(
    label="Please describe what happened and include all details in your complaint",
    placeholder="Type multiple lines here...",
    height=200
)

complaint_word_count = len(consumer_complaint_narrative.split())

if "$" in consumer_complaint_narrative:
    dollar_sign=1
else:
    dollar_sign=0

critical_severity_keywords = ['foreclosure', 'eviction', 'bankruptcy', 'homeless', 'sheriff sale', 'lease termination', 'padlock', 'shelter', 'garnishment', 'attorney general', 'summons', 'court order', 'judgment', 'wage attachment', 'poverty', 'destitute', 'hardship', 'suicidal']

if any(keyword in consumer_complaint_narrative for keyword in critical_severity_keywords):
    critical_severity=1
else:
    critical_severity=0

high_severity_keywords = ['fraud', 'scam', 'unauthorized transaction', 'account takeover', 'phishing', 'impersonation', 'forgery', 'closed account', 'repossession', 'collections', 'frozen account', 'account lock', 'charge off', 'predatory lending', 'harassment']

if any(keyword in consumer_complaint_narrative for keyword in high_severity_keywords):
    high_severity=1
else:
    high_severity=0

medium_severity_keywords = ['credit score', 'dispute', 'fcra', 'late fee', 'hidden charge', 'interest rate increase', 'billing error', 'escrow shortage']

if any(keyword in consumer_complaint_narrative for keyword in medium_severity_keywords):
    medium_severity=1
else:
    medium_severity=0
    
legal_risk_keywords = ['lawsuit', 'attorney', 'lawyer', 'court', 'subpoena', 'legal action', 'suing', 'fcra violation', 'fdcpa', 'tcpa', 'regulatory complaint']
    
if any(keyword in consumer_complaint_narrative for keyword in legal_risk_keywords):
    legal_risk=1
else:
    legal_risk=0

financial_loss_keywords = ['stolen funds', 'overdraft fee', 'unauthorized charge', 'drained account', 'wire fraud', 'double charged', 'seized funds', 'unauthorized fee']
    
if any(keyword in consumer_complaint_narrative for keyword in financial_loss_keywords):
    financial_loss=1
else:
    financial_loss=0

credit_damage_keywords = ['credit score dropped', 'incorrect reporting', 'derogatory mark', 'late payment reported', 'identity theft', 'mixed file', 'unverified debt']

if any(keyword in consumer_complaint_narrative for keyword in credit_damage_keywords):
    credit_damage=1
else:
    credit_damage=0

model = st.radio(
    label="Which predictive model to use for scoring?",
    options=['Logistic Regression', 'Gradient Boosting', 'Random Forest'],
    index=0
)

feature_vector = [Product_Checking_or_savings_account, Product_Credit_card, Product_Debt_collection, Product_Debt_or_credit_management, Product_Money_transfer_virtual_currency, Product_Mortgage, Product_Payday_loan_title_loan, Product_Prepaid_card, Product_Student_loan, Product_Vehicle_loan_or_lease, Older_American, Servicemember, complaint_word_count, dollar_sign, critical_severity, high_severity, medium_severity, financial_loss, credit_damage, credit_bureau, credit_union, southern_state]

# Process and score the observation
if st.button("Score using Model"):
    
    # Create input DataFrame matching training feature names
    input_data = pd.DataFrame([feature_vector], columns=['Product_Checking_or_savings_account', 'Product_Credit_card', 'Product_Debt_collection', 'Product_Debt_or_credit_management','Product_Money_transfer_virtual_currency_or_money_service', 'Product_Mortgage', 'Product_Payday_loan_title_loan_personal_loan_or_advance_loan','Product_Prepaid_card', 'Product_Student_loan', 'Product_Vehicle_loan_or_lease', 'Older_American', 'Servicemember', 'complaint_word_count', 'dollar_sign', 'critical_severity_keywords','high_severity_keywords', 'medium_severity_keywords', 'financial_loss_keywords', 'credit_damage_keywords', 'credit_bureau', 'credit_union', 'Southern_State'])
    
    # Run prediction for scoring
    if (model=='Logistic Regression'):
        prediction = logistic_reg_sklearn_model.predict(input_data)
        prediction_proba = logistic_reg_sklearn_model.predict_proba(input_data) if hasattr(logistic_reg_sklearn_model, "predict_proba") else None
    elif (model=='Gradient Boosting'):
        prediction = grad_boost_sklearn_model.predict(input_data)
        prediction_proba = grad_boost_sklearn_model.predict_proba(input_data) if hasattr(grad_boost_sklearn_model, "predict_proba") else None
    elif (model=='Random Forest'):
        prediction = random_forest_sklearn_model.predict(input_data)
        prediction_proba = random_forest_sklearn_model.predict_proba(input_data) if hasattr(random_forest_sklearn_model, "predict_proba") else None
    else: 
        prediction = None
        prediction_proba = None
    
    # Display results
    if (model=='Logistic Regression'):
        st.success(f"Logistic Regression Model Prediction Result")
    elif (model=='Gradient Boosting'):
        st.success(f"Gradient Boosting Model Prediction Result")
    elif (model=='Random Forest'):
        st.success(f"Random Forest Model Prediction Result")
    else: 
        st.success(f"No Model Prediction Result")
    if prediction_proba is not None:
        st.write(f"Likelihood of a respectful closure to this complaint: {prediction_proba[0].max()*100:.1f}%")