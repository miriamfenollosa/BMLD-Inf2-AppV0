import streamlit as st
import views.home
import views.noten_berechner

tab1, tab2 = st.tabs(["🏠 Home", "Notenrechner"])

with tab1:
    views.home.display()  # Hier wird die Home-Funktion aufgerufen

with tab2:
    views.noten_berechner.main()  # Wir nehmen an, dass du in noten_berechnen eine Funktion `main()` definierst, die den Streamlit-Code enthält
