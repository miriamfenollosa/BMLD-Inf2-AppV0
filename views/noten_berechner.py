import streamlit as st
from functions.notenberechner import berechne_note

def main():

    st.title("Schweizer Notenrechner")

    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

    if st.button("Note berechnen"):
        note = berechne_note(punkte, max_punkte)
        st.success(f"Deine Note ist: {note}")
