import streamlit as st
import pandas as pd
import pickle

# Load the trained model outside the button click for efficiency
model = pickle.load(open("rf_100_model.pkl", "rb"))

# Title and description of the app
st.title("💳 Credit Card Fraud Detection")
st.markdown("""
### Welcome to the Credit Card Fraud Detection App!
This tool uses a trained machine learning model to predict if a credit card transaction is **fraudulent** or **safe** based on various features.

Fill in the details below to get a prediction.
""")

# Divider for better UI
st.markdown("---")

# Section header for user inputs
st.subheader("🔍 Transaction Details")

# User inputs for the selected features (grouped and formatted)
col1, col2, col3 = st.columns(3)
with col1:
    V1 = st.number_input("V1", min_value=-10.0, max_value=10.0, value=0.0)
    V4 = st.number_input("V4", min_value=-10.0, max_value=10.0, value=0.0)
    V8 = st.number_input("V8", min_value=-10.0, max_value=10.0, value=0.0)
    V14 = st.number_input("V14", min_value=-10.0, max_value=10.0, value=0.0)

with col2:
    V3 = st.number_input("V3", min_value=-10.0, max_value=10.0, value=0.0)
    V9 = st.number_input("V9", min_value=-10.0, max_value=10.0, value=0.0)
    V12 = st.number_input("V12", min_value=-10.0, max_value=10.0, value=0.0)
    V17 = st.number_input("V17", min_value=-10.0, max_value=10.0, value=0.0)

with col3:
    V10 = st.number_input("V10", min_value=-10.0, max_value=10.0, value=0.0)
    V11 = st.number_input("V11", min_value=-10.0, max_value=10.0, value=0.0)
    V13 = st.number_input("V13", min_value=-10.0, max_value=10.0, value=0.0)
    V22 = st.number_input("V22", min_value=-10.0, max_value=10.0, value=0.0)
    V28 = st.number_input("V28", min_value=-10.0, max_value=10.0, value=0.0)

# Time and Amount inputs at the bottom
Time = st.number_input("⏲️ Time (in seconds)", min_value=0, max_value=86400, value=0)
Amount = st.number_input("💵 Amount", min_value=0.0, value=0.0)

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
st.markdown("---")
if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_data)
    st.markdown("### 💡 Prediction Result:")
    if prediction[0] == 1:
        st.error("🚨 **Fraudulent Transaction Detected!**")
    else:
        st.success("✅ **Transaction is Safe.**")

# Footer
st.markdown("---")
st.markdown("App powered by a machine learning model trained for fraud detection.")
