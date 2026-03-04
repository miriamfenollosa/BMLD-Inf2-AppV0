import streamlit as st
from functions.notenberechner import percent_to_swiss_grade, weighted_average
st.title("Unterseite A")

st.write("Diese Seite ist eine Unterseite der Startseite.")

with st.form("noten_form"):
    prozent = st.number_input("Prozent (0-100)", min_value=0.0, max_value=100.0, step=0.1, key="percent")
    st.text_input("Noten (1.0-6.0, durch Komman getrennt)", key="grades")
    st.write(percent_to_swiss_grade(prozent))

   st.form_submit_button("Berechnen")