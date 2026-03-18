import pandas as pd
import streamlit as st
from utils.data_manager import DataManager
from functions.notenberechner import berechne_note

def main():
    st.title("Notenrechner (nach Schweizer Notensystem)")

    st.markdown("**Hinweis:** Die Note wird nach dem Schweizer Notensystem berechnet, wobei 1 die schlechteste Note und 6 die beste Note ist.")
    
    st.write("Gib deine erreichten Punkte und die maximale Punktzahl ein, um deine Note zu berechnen.")
    
    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

    if 'data' not in st.session_state:
        st.session_state['data'] = []

    if st.button("Note berechnen"):
        result = berechne_note(punkte, max_punkte)
        st.success(f"Deine Note ist: {result['note']}")
        
        # Speichere das Dictionary im Session State
        st.session_state['data'].append(result)

    # --- CODE UPDATE: save data to data manager ---
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
    # --- END OF CODE UPDATE ---

    # Zeige die Tabelle an, wenn es Daten gibt
    if st.session_state['data']:
        df = pd.DataFrame(st.session_state['data'])
        st.dataframe(df)

