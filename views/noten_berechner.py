import streamlit as st
from functions.notenberechner import berechne_note

def main():

    st.title("Notenrechner (nach Schweizer Notensystem)")

    st.write("Gib deine erreichten Punkte und die maximale Punktzahl ein, um deine Note zu berechnen.")

    st.markdown("**Hinweis:** Die Note wird nach dem Schweizer Notensystem berechnet, wobei 1 die schlechteste Note und 6 die beste Note ist.")

    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

    if st.button("Note berechnen"):
        note = berechne_note(punkte, max_punkte)
        st.success(f"Deine Note ist: {note}")
