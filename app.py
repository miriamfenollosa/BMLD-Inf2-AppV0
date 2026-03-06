import streamlit as st
import views.home
import views.noten_berechner

tab1, tab2 = st.tabs(["🏠 Home", "Notenrechner"])

with tab1:
    views.home.display()

with tab2:
    views.noten_berechner.main()
