import streamlit as st

# 1. YOUR FUNCTION (The Logic)
def calculate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90: return "A"
    if percentage >= 80: return "B"
    if percentage >= 70: return "C"
    if percentage >= 60: return "D" 
    if percentage < 60: return "F"s

# 2. THE VIEW (The UI)
st.title("My Grade App")

# Create the inputs
user_score = st.number_input("Enter Score")
max_score = st.number_input("Enter Max Points", value=100)

# Trigger the function with a button
if st.button("Calculate"):
    # Call your function using the variables from the widgets
    result = calculate_grade(user_score, max_score)
    
    # Display the result
    st.write(f"Your final grade is: **{result}**")