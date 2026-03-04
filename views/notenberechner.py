import streamlit as st

# 1. YOUR FUNCTION (The Logic)
def calculate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90: return "A"
    if percentage >= 80: return "B"
    return "C"

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

    with st.form("grade_form"):
    score = st.number_input("Score")
    total = st.number_input("Total")
    
    # The submit button
    submitted = st.form_submit_button("Calculate")
    
    if submitted:
        # Only runs once the button is clicked
        final_grade = calculate_grade(score, total)
        st.success(f"Done! Grade: {final_grade}")