# ...existing code...
import streamlit as st

st.set_page_config(page_title="Notenberechner (CH)", page_icon="🎓")

st.title("🎓 Notenberechner (Schweizer System)")
st.write("Gib die erreichten Punkte und die maximale Punktzahl ein. Die Note wird nach der Formel (erreichte/gesamt)*5 + 1 berechnet (1.0–6.0, 4.0 = bestanden).")

col1, col2 = st.columns(2)

with col1:
    score = st.number_input("Erreichte Punkte", min_value=0.0, value=0.0, step=0.5, format="%.2f")
with col2:
    total = st.number_input("Maximale Punktzahl", min_value=1.0, value=100.0, step=1.0, format="%.2f")

if total <= 0:
    st.error("Die maximale Punktzahl muss grösser als 0 sein.")
else:
    percentage = (score / total) * 100.0

    # Formel: 1.0 bei 0% bis 6.0 bei 100% -> Note = 1 + (erreichte/gesamt)*5
    raw_grade = 1.0 + (score / total) * 5.0
    grade = max(1.0, min(6.0, raw_grade))
    grade_display = round(grade, 1)

    passed = grade >= 4.0

    st.divider()
    st.subheader(f"Note: {grade_display} {'(bestanden)' if passed else '(nicht bestanden)'}")
    st.progress(min(max(percentage / 100.0, 0.0), 1.0))
    st.write(f"Prozent: **{percentage:.2f}%**")

    if passed:
        st.success("Bestanden 🎉")
        st.balloons()
    else:
        st.error("Nicht bestanden — weiter üben!")
# ...existing code...