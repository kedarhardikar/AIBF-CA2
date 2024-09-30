import streamlit as st
import joblib
import pandas as pd

# Load the trained model
rf_100 = joblib.load('rf_100_model.pkl')

# Title of the app
st.title("Credit Card Fraud Detection")

# User inputs for the selected features
V1 = st.number_input("V1", min_value=-10.0, max_value=10.0, value=0.0)
V3 = st.number_input("V3", min_value=-10.0, max_value=10.0, value=0.0)
V4 = st.number_input("V4", min_value=-10.0, max_value=10.0, value=0.0)
V8 = st.number_input("V8", min_value=-10.0, max_value=10.0, value=0.0)
V9 = st.number_input("V9", min_value=-10.0, max_value=10.0, value=0.0)
V10 = st.number_input("V10", min_value=-10.0, max_value=10.0, value=0.0)
V11 = st.number_input("V11", min_value=-10.0, max_value=10.0, value=0.0)
V12 = st.number_input("V12", min_value=-10.0, max_value=10.0, value=0.0)
V14 = st.number_input("V14", min_value=-10.0, max_value=10.0, value=0.0)
V17 = st.number_input("V17", min_value=-10.0, max_value=10.0, value=0.0)
V22 = st.number_input("V22", min_value=-10.0, max_value=10.0, value=0.0)
V28 = st.number_input("V28", min_value=-10.0, max_value=10.0, value=0.0)
V13 = st.number_input("V13", min_value=-10.0, max_value=10.0, value=0.0)
Time = st.number_input("Time", min_value=0, max_value=86400, value=0)
Amount = st.number_input("Amount", min_value=0.0, value=0.0)

# Create a DataFrame with the input values
input_data = pd.DataFrame({
    'V14': [V14],
    'V17': [V17],
    'V10': [V10],
    'V12': [V12],
    'V4': [V4],
    'V11': [V11],
    'V9': [V9],
    'V3': [V3],
    'Time': [Time],
    'V8': [V8],
    'V1': [V1],
    'V28': [V28],
    'V22': [V22],
    
    'V13': [V13],
    
    'Amount': [Amount]
})

# Button to trigger prediction
if st.button("Predict"):
    prediction = rf_100.predict(input_data)
    if prediction[0] == 1:
        st.error("Fraudulent Transaction!")
    else:
        st.success("Safe Transaction.")




