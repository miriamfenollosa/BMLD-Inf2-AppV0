st.title("Schweizer Notenrechner")

punkte = st.number_input("Erreichte Punkte", min_value=0, step=1)
max_punkte = st.number_input("Maximale Punkte", min_value=1, step=1)

note = berechne_note(punkte, max_punkte)

st.write(f"Deine Note: {note}")