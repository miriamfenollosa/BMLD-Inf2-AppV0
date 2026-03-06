import streamlit as st
import views.home  # Hier importieren wir das ganze Home-Modul

tab1, tab2 = st.tabs(["🏠 Home", "Notenrechner"])

with tab1:
    views.home.display()  # Wir rufen eine Funktion aus home.py auf, die den Inhalt rendert

with tab2:
    import streamlit as st
    from functions.notenberechner import berechne_note

    st.title("Notenrechner")

    with st.form("noten_form"):
        punkte = st.number_input("Erreichte Punkte", min_value=0)
        max_punkte = st.number_input("Maximale Punkte", min_value=1)
        submit = st.form_submit_button("Note berechnen")

    if submit:
        note = berechne_note(punkte, max_punkte)
        st.success(f"Deine Note ist: {note}")
