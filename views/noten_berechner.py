import streamlit as st

st.set_page_config(page_title="Notenberechner (CH)")

st.title("Notenberechner (Schweizer System)")

score = st.number_input("Erreichte Punkte", min_value=0.0, value=0.0, format="%.2f")
total = st.number_input("Maximale Punktzahl", min_value=1.0, value=100.0, format="%.2f")

if total <= 0:
    st.error("Maximale Punktzahl muss grösser als 0 sein.")
elif score < 0:
    st.error("Erreichte Punkte dürfen nicht negativ sein.")
else:
    grade = 1.0 + (score / total) * 5.0
    grade = max(1.0, min(6.0, grade))
    st.write("Note:", round(grade, 1))