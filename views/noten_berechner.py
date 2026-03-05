import streamlit as st

st.set_page_config(page_title="Notenberechner (CH)", page_icon="🎓")
st.title("Notenberechner (Schweizer System)")
st.write("Gib erreichte Punkte und maximale Punktzahl ein. Note = (erreichte/gesamt)*5 + 1 (Skala 1.0–6.0, 4.0 = bestanden).")

def calculate_grade(score, total):
    if total <= 0:
        raise ValueError("Maximale Punktzahl muss > 0 sein.")
    if score < 0:
        raise ValueError("Erreichte Punkte dürfen nicht negativ sein.")
    raw = 1.0 + (score / total) * 5.0
    return max(1.0, min(6.0, raw))

col1, col2 = st.columns(2)
with col1:
    user_score = st.number_input("Erreichte Punkte", min_value=0.0, value=0.0, step=0.5, format="%.2f")
with col2:
    max_score = st.number_input("Maximale Punktzahl", min_value=1.0, value=100.0, step=1.0, format="%.2f")

if st.button("Berechnen"):
    try:
        grade = calculate_grade(user_score, max_score)
    except ValueError as e:
        st.error(str(e))
    else:
        percentage = max(0.0, min(100.0, (user_score / max_score) * 100.0))
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