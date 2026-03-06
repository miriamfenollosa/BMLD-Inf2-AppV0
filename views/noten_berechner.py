import streamlit as st
from functions.notenberechner import berechne_note

st.title("Schweizer Notenrechner")

with st.form("noten_form"):
    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

    submit = st.form_submit_button("Note berechnen")

if submit:
    note = berechne_note(punkte, max_punkte)
    st.success(f"Deine Note ist: {note}")
