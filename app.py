
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("anemia_model.pkl")

st.title("Anemia Risk Prediction Dashboard")

# Collect user inputs
year = st.number_input("Year", 2000, 2030, value=2025)
prevalence_reproductive = st.number_input("Prevalence (Reproductive-age women %)", 0.0, 100.0, 35.0)
prevalence_nonpreg = st.number_input("Prevalence (Non-pregnant women %)", 0.0, 100.0, 34.0)
prevalence_children = st.number_input("Prevalence (Children %)", 0.0, 100.0, 40.0)

# Convert inputs to DataFrame with same feature names
X_input = pd.DataFrame({
    'Year': [year],
    'Prevalence_reproductive': [prevalence_reproductive],
    'Prevalence_nonpreg': [prevalence_nonpreg],
    'Prevalence_children': [prevalence_children]
})

# Predict anemia risk
if st.button("Predict Anemia Risk"):
    # Model prediction (overall)
    prediction = model.predict(X_input)[0]
    
    # Threshold-based per-group check
    threshold = 40
    risk_dict = {
        'Reproductive-age women': 'Yes' if prevalence_reproductive > threshold else 'No',
        'Non-pregnant women': 'Yes' if prevalence_nonpreg > threshold else 'No',
        'Children': 'Yes' if prevalence_children > threshold else 'No'
    }
    
    # Display individual group risk
    st.write("### Predicted High Anemia Risk per Group:")
    for group, risk in risk_dict.items():
        st.write(f"{group}: {risk}")
    
    # Summary message
    high_risk_groups = [g for g, r in risk_dict.items() if r == "Yes"]
    if len(high_risk_groups) == 0:
        st.write("No group is at high anemia risk.")
    elif len(high_risk_groups) == 1:
        st.write(f"High anemia risk detected in: {high_risk_groups[0]}")
    elif len(high_risk_groups) == 2:
        st.write(f"High anemia risk detected in: {high_risk_groups[0]} and {high_risk_groups[1]}")
    else:
        st.write("High anemia risk detected in all three groups: Reproductive-age women, Non-pregnant women, and Children")
    
    # Overall model prediction
    #st.success(f"Overall Predicted High Anemia Risk (model): {'Yes' if prediction==1 else 'No'}")

