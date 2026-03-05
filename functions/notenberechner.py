import streamlit as st

# Funktion zur Berechnung der Note
def berechne_note(punkte, max_punkte):
    if max_punkte == 0:
        return "Maximale Punktzahl darf nicht 0 sein"
    prozent = (punkte / max_punkte) * 5 + 1
    note = round(prozent, 1)
    return note