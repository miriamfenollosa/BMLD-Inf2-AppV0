import streamlit as st
import views.home
import views.noten_berechner
import pandas as pd

# --- NEW CODE: initialize empty data frame if not already present ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame()
# --- END OF NEW CODE ---

tab1, tab2 = st.tabs(["🏠 Home", "Notenrechner"])

with tab1:
    views.home.display()

with tab2:
    views.noten_berechner.main()
