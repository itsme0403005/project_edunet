import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

# Mappings used during label encoding
workclass_map = {'Private': 4, 'Self-emp-not-inc': 5, 'Local-gov': 2, 'State-gov': 6, 'Federal-gov': 1, 'Self-emp-inc': 7}
marital_map = {'Married-civ-spouse': 2, 'Never-married': 4, 'Divorced': 1, 'Separated': 5, 'Widowed': 6, 'Married-spouse-absent': 3}
occupation_map = {'Prof-specialty': 9, 'Craft-repair': 2, 'Exec-managerial': 4, 'Adm-clerical': 0, 'Sales': 11, 
                  'Other-service': 8, 'Machine-op-inspct': 7, 'Transport-moving': 13, 'Handlers-cleaners': 5,
                  'Tech-support': 12, 'Farming-fishing': 3, 'Protective-serv': 10, 'Priv-house-serv': 6}
gender_map = {'Male': 1, 'Female': 0}
education_map = {
    'Preschool': 1, '1st-4th': 2, '5th-6th': 3, '7th-8th': 4, '9th': 5,
    '10th': 6, '11th': 7, '12th': 8, 'HS-grad': 9, 'Some-college': 10,
    'Assoc-voc': 11, 'Assoc-acdm': 12, 'Bachelors': 13, 'Masters': 14,
    'Prof-school': 15, 'Doctorate': 16
}

def reverse_map(mapping, label):
    return mapping.get(label, 0)

st.set_page_config(page_title="Income Prediction App", layout="centered")

st.title("Salary  Prediction Web App")
st.write("This app predicts whether a person earns more than 50K per year.")

with st.form("user_input_form"):
    age = st.slider("Age", 18, 75, 30)
    workclass = st.selectbox("Workclass", list(workclass_map.keys()))
    education = st.selectbox("Education Level", list(education_map.keys()))
    marital_status = st.selectbox("Marital Status", list(marital_map.keys()))
    occupation = st.selectbox("Occupation", list(occupation_map.keys()))
    gender = st.selectbox("Gender", list(gender_map.keys()))
    capital_gain = st.number_input("Capital Gain", min_value=0, max_value=99999, value=0)
    capital_loss = st.number_input("Capital Loss", min_value=0, max_value=99999, value=0)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)
    submitted = st.form_submit_button("Predict Income")

if submitted:
    input_data = pd.DataFrame([{
        'age': age,
        'workclass': reverse_map(workclass_map, workclass),
        'educational-num': education_map[education],
        'marital-status': reverse_map(marital_map, marital_status),
        'occupation': reverse_map(occupation_map, occupation),
        'gender': reverse_map(gender_map, gender),
        'capital-gain': capital_gain,
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week
    }])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Income: {prediction}")
