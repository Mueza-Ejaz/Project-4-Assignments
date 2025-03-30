import streamlit as st

st.set_page_config(
    page_title="BMI-Calculator", 
    page_icon=" 🚻 ",  # This sets a small favicon icon (optional)
    layout="centered"    # Options: "centered" (default) or "wide"
)

# Title:
st.title("BMI-Calculator")

# Input Fields:
weight = st.number_input("Enter your weight (kg):", min_value = 1.0, step = 0.1)
height = st.number_input("Enter your height (inches):", min_value = 1.0, step = 0.1)

# 1 inch = 0.0254 meters 

# Convert height to meters
height_meters = height * 0.0254

# Calculate BMI:
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            st.warning("Underweight")
        elif bmi < 24.9:
            st.success("Normal weight")
        elif bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")
    else:
        st.error("Height must be greater than zero!")



