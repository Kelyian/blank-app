import streamlit as st

st.title("Title : Bio data")
st.write("This is a sample web app")

first_name = st.text_input("First name")
last_name = st.text_input("Last name")
gender = st.selectbox("Gender", ["Male","Female"])
age = st.number_input("Age", min_value=0, max_value=120, step=1)
dob = st.date_input("Your date of birth")
Marital_status = st.radio("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
Years_of_experience = st.slider("Years of Experience", 0, 50)