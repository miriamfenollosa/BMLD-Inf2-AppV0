# ...existing code...
"""
Notenberechner (Schweizer Skala 1.0 - 6.0)

Funktionen:
- percent_to_swiss_grade(percent, round_to=0.1)
- weighted_average(grades, weights=None, round_to=0.1)
- notenberechner()  # interaktive CLI
"""
from typing import Iterable, Optional


def _clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def _to_float(value) -> float:
    """Konvertiert Zahl/Str (auch mit Komma) zu float, wirft ValueError bei ungültig."""
    if isinstance(value, str):
        value = value.strip().replace(",", ".")
    return float(value)


def percent_to_swiss_grade(percent, round_to: float = 0.1) -> float:
    """
    Konvertiert Prozent (0-100) in Schweizer Note (1.0 - 6.0).
    Linear: 0% -> 1.0, 100% -> 6.0. Ergebnis auf `round_to` runden (z.B. 0.1).
    """
    try:
        p = _to_float(percent)
    except (TypeError, ValueError):
        raise ValueError("percent muss eine Zahl sein (z.B. 75 oder '75' oder '75,0')")
    p = _clamp(p, 0.0, 100.0)
    grade = 1.0 + (p / 100.0) * 5.0
    if round_to:
        factor = 1.0 / float(round_to)
        grade = round(grade * factor) / factor
    return _clamp(grade, 1.0, 6.0)


def weighted_average(grades: Iterable, weights: Optional[Iterable] = None, round_to: float = 0.1) -> float:
    """
    Berechnet gewichteten Durchschnitt aus Schweizer Noten (1.0-6.0).
    grades: Iterable von Zahlen oder Strings (z.B. [5.5, '4', '6'])
    weights: Iterable gleicher Länge oder None (dann gleiche Gewichte).
    Ergebnis gerundet auf `round_to`.
    """
    g_list = list(grades)
    if not g_list:
        raise ValueError("grades-Liste darf nicht leer sein")
    try:
        g = [ _clamp(_to_float(x), 1.0, 6.0) for x in g_list ]
    except (TypeError, ValueError):
        raise ValueError("Alle grades müssen Zahlen sein (z.B. 5.5 oder '5,5')")

    if weights is None:
        w = [1.0] * len(g)
    else:
        w_list = list(weights)
        if len(w_list) != len(g):
            raise ValueError("weights muss die gleiche Länge wie grades haben")
        try:
            w = [ float(_to_float(x)) for x in w_list ]
        except (TypeError, ValueError):
            raise ValueError("Alle weights müssen Zahlen sein")
    total_w = sum(w)
    if total_w == 0:
        raise ValueError("Summe der Gewichte darf nicht 0 sein")
    mean = sum(gi * wi for gi, wi in zip(g, w)) / total_w
    if round_to:
        factor = 1.0 / float(round_to)
        mean = round(mean * factor) / factor
    return _clamp(mean, 1.0, 6.0)


def notenberechner():
    """
    Einfache Kommandozeilen-Bedienung:
    1) Prozent -> Note
    2) Gewichteter Notendurchschnitt
    """
    print("Notenberechner (Schweizer Skala 1.0 - 6.0)")
    print("1) Prozent -> Note")
    print("2) Gewichteter Durchschnitt aus Noten")
    mode = input("Modus wählen (1/2): ").strip()
    if mode == "1":
        p = input("Prozent (0-100): ").strip()
        try:
            note = percent_to_swiss_grade(p)
            print(f"Note: {note:.1f}")
        except ValueError as e:
            print("Fehler:", e)
    elif mode == "2":
        gs = input("Noten eingeben, getrennt durch Leerzeichen (z.B. 5.5 4 6): ").strip().split()
        if not gs:
            print("Keine Noten eingegeben.")
            return
        ws_raw = input("Gewichte eingeben (optional, gleiche Anzahl), getrennt durch Leerzeichen, oder Enter für gleiche Gewichte: ").strip()
        try:
            if ws_raw:
                weights = ws_raw.split()
                result = weighted_average(gs, weights)
            else:
                result = weighted_average(gs, None)
            print(f"Gewichteter Durchschnitt: {result:.1f}")
        except ValueError as e:
            print("Fehler:", e)
    else:
        print("Ungültige Auswahl.")


if __name__ == "__main__":
    notenberechner()
# ...existing code...