import streamlit as st

st.set_page_config(page_title="Easy Grade Calc", page_icon="🎓")

st.title("🎓 Simple Grade Calculator")
st.write("Enter your scores below to see your final grade.")

col1, col2 = st.columns(2)

with col1:
    score = st.number_input("Your Score:", min_value=0.0, value=85.0)

with col2:
    # Increased max_value to 1000 just in case!
    total = st.number_input("Total Possible Points:", min_value=1.0, max_value=1000.0, value=100.0)

# The Logic
percentage = (score / total) * 100

if percentage >= 90:
    grade, color = "A", "green"
elif percentage >= 80:
    grade, color = "B", "blue"
elif percentage >= 70:
    grade, color = "C", "orange" # Fixed here
elif percentage >= 60:
    grade, color = "D", "orange"
else:
    grade, color = "F", "red"

# Display the Result
st.divider()
# Use a cap of 1.0 for the progress bar to avoid errors if percentage > 100
st.progress(min(percentage / 100, 1.0))

st.subheader(f"Your Result: :{color}[{grade}]")
st.write(f"You scored **{percentage:.2f}%**")

if percentage >= 60:
    st.balloons()
    st.success("Congratulations! You passed.")
else:
    st.error("Keep studying! You'll get it next time.")