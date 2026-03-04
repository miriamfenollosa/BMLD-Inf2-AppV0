import streamlit as st

st.set_page_config(page_title="Easy Grade Calc", page_icon="🎓")

st.title("🎓 Simple Grade Calculator")
st.write("Enter your scores below to see your final grade.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    score = st.number_input("Your Score:", min_value=0.0, max_value=100.0, value=85.0)

with col2:
    total = st.number_input("Total Possible Points:", min_value=1.0, max_value=100.0, value=100.0)

# The Logic
percentage = (score / total) * 100

if percentage >= 90:
    grade = "A"
    color = "green"
elif percentage >= 80:
    grade = "B"
    color = "blue"
elif percentage >= 70:
    grade = "orange" # Using orange for C
    grade = "C"
elif percentage >= 60:
    grade = "D"
    color = "orange"
else:
    grade = "F"
    color = "red"

# Display the Result
st.divider()
st.subheader(f"Your Result: :{color}[{grade}]")
st.progress(percentage / 100)
st.write(f"You scored **{percentage:.2f}%**")

if percentage >= 60:
    st.balloons()
    st.success("Congratulations! You passed.")
else:
    st.error("Keep studying! You'll get it next time.")