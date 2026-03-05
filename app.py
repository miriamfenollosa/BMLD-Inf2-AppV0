import streamlit as st
from functions.notenberechner import berechne_note

st.sidebar.title("Navigation")
seite = st.sidebar.radio("Wähle eine Seite", ["Startseite", "Notenrechner"])

if seite == "Startseite":
    st.title("Willkommen zu meiner App")
    st.write("Hier findest du eine Übersicht über die Funktionen dieser Anwendung. Sie hilft dir, deine Punktzahlen nach dem Schweizer Schulsystem zu berechnen. Wähle dazu die entsprechende Seite in der Navigation.")
    # Hier kannst du weitere Inhalte einfügen, z.B. Bilder oder Links.

elif seite == "Notenrechner":
    st.title("Schweizer Notenrechner")

    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

    note = berechne_note(punkte, max_punkte)

    st.write(f"Deine Note: {note}")
