import streamlit as st
from functions.notenberechner import percent_to_swiss_grade, weighted_average
st.title("Unterseite A")

st.write("Diese Seite ist eine Unterseite der Startseite.")

with st.form("noten_form"):
    prozent = st.number_input("Prozent (0-100)", min_value=0.0, max_value=100.0, step=0.1, key="percent")
    st.text_input("Noten (1.0-6.0, durch Komman getrennt)", key="grades")
    st.write(percent_to_swiss_grade(prozent))

    # ...existing code...
import re
import streamlit as st
from functions.notenberechner import percent_to_swiss_grade, weighted_average

st.title("Notenberechner (Schweizer Skala 1.0 - 6.0)")

st.write("Gib Prozent oder eine Liste von Noten ein. Noten können Dezimaltrennzeichen Komma oder Punkt verwenden.")

def _extract_numbers(text: str):
    """Findet Zahlen mit optionalem Dezimaltrennzeichen (Komma oder Punkt)."""
    if not text:
        return []
    matches = re.findall(r"[-+]?\d+[.,]?\d*", text)
    return [m.replace(",", ".") for m in matches]

with st.form("noten_form"):
    prozent = st.number_input("Prozent (0-100)", min_value=0.0, max_value=100.0, step=0.1, key="percent")
    grades_text = st.text_input("Noten (z.B. 5.5, 4, 6 oder 5,5 4 6)", key="grades")
    weights_text = st.text_input("Gewichte (optional, gleiche Anzahl wie Noten)", key="weights")
    submit = st.form_submit_button("Berechnen")

if submit:
    # Prozent -> Note
    try:
        note_from_percent = percent_to_swiss_grade(prozent)
        st.success(f"Aus {prozent:.1f}% ergibt sich Note: {note_from_percent:.1f}")
    except Exception as e:
        st.error(f"Fehler bei Prozent-Umrechnung: {e}")

    # Notenliste -> gewichteter Durchschnitt (falls angegeben)
    nums = _extract_numbers(grades_text)
    if nums:
        try:
            grades = [float(x) for x in nums]
            weights = None
            w_nums = _extract_numbers(weights_text)
            if w_nums:
                weights = [float(x) for x in w_nums]
            avg = weighted_average(grades, weights)
            st.info(f"Gewichteter Durchschnitt aus Noten: {avg:.1f}")
        except Exception as e:
            st.error(f"Fehler beim Berechnen des Durchschnitts: {e}")
    else:
        st.write("Keine Noten eingegeben.")
# ...existing code...