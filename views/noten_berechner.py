import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from utils.data_manager import DataManager
from functions.notenberechner import berechne_note

def main():
    st.title("Notenrechner (nach Schweizer Notensystem)")

    st.markdown("**Hinweis:** Die Note wird nach dem Schweizer Notensystem berechnet, wobei 1 die schlechteste Note und 6 die beste Note ist.")
    
    st.write("Gib deine erreichten Punkte und die maximale Punktzahl ein, um deine Note zu berechnen.")
    
    punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
    max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)
    if 'data_df' not in st.session_state:
        st.session_state['data_df'] = pd.DataFrame()

        noten = [int(wert) for wert in [5, 4, 6, 5]]  # oder aus der App gesammelt
        labels = ["A", "B", "C", "D"]

        plt.figure(figsize=(7, 4))
        plt.plot(labels, noten, marker="o", linestyle="-", color="magenta")
        plt.title("Meine Daten als Linie")
        plt.savefig("noten_linien.png")
        plt.show()

    #if 'data' not in st.session_state:
     #   st.session_state['data'] = []

    if st.button("Note berechnen"):
        result = berechne_note(punkte, max_punkte)
        st.success(f"Deine Note ist: {result['note']}")
        
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])])

        # --- CODE UPDATE: save data to data manager ---
        data_manager = DataManager()
        data_manager.save_user_data(st.session_state['data_df'], 'data.csv')
        # --- END OF CODE UPDATE ---

        st.line_chart(st.session_state['data_df'].set_index('timestamp')['note'])

        st.dataframe(st.session_state['data_df'])


