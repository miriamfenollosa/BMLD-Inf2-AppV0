# ...existing code...
def notenberechner
# ...existing code...
def _clamp(x, lo, hi):
    return max(lo, min(hi, x))

def percent_to_swiss_grade(percent, round_to=0.1):
    """
    Konvertiert Prozent (0-100) in Schweizer Note (1.0 - 6.0).
    Linear: 0% -> 1.0, 100% -> 6.0. Ergebnis auf `round_to` runden (z.B. 0.1).
    """
    try:
        p = float(percent)
    except (TypeError, ValueError):
        raise ValueError("percent muss eine Zahl sein")
    p = _clamp(p, 0.0, 100.0)
    grade = 1.0 + (p / 100.0) * 5.0
    if round_to:
        factor = 1.0 / float(round_to)
        grade = round(grade * factor) / factor
    return _clamp(grade, 1.0, 6.0)

def weighted_average(grades, weights=None, round_to=0.1):
    """
    Berechnet gewichteten Durchschnitt aus Schweizer Noten (1.0-6.0).
    grades: Liste von Zahlen (z.B. [5.5, 4.0, 6.0])
    weights: Liste gleicher Länge oder None (dann gleiche Gewichte).
    Ergebnis gerundet auf `round_to`.
    """
    if not grades:
        raise ValueError("grades-Liste darf nicht leer sein")
    g = [float(x) for x in grades]
    if weights is None:
        w = [1.0] * len(g)
    else:
        if len(weights) != len(g):
            raise ValueError("weights muss die gleiche Länge wie grades haben")
        w = [float(x) for x in weights]
    total_w = sum(w)
    if total_w == 0:
        raise ValueError("Summe der Gewichte darf nicht 0 sein")
    mean = sum(gi * wi for gi, wi in zip(g, w)) / total_w
    if round_to:
        factor = 1.0 / float(round_to)
        mean = round(mean * factor) / factor
    return _clamp(mean, 1.0, 6.0)

def notenberechner_interactive():
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
        ws = input("Gewichte eingeben (optional, gleiche Anzahl), getrennt durch Leerzeichen, oder Enter für gleiche Gewichte: ").strip()
        try:
            if ws:
                weights = ws.split()
                result = weighted_average(gs, weights)
            else:
                result = weighted_average(gs, None)
            print(f"Gewichteter Durchschnitt: {result:.1f}")
        except ValueError as e:
            print("Fehler:", e)
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    notenberechner_interactive()
```# filepath: /Users/miriamfenollosa/Desktop/Informatik 2/Übung_02/BMLD-Inf2-AppV0/functions/notenberechner.py
# ...existing code...
def notenberechner
# ...existing code...
def _clamp(x, lo, hi):
    return max(lo, min(hi, x))

def percent_to_swiss_grade(percent, round_to=0.1):
    """
    Konvertiert Prozent (0-100) in Schweizer Note (1.0 - 6.0).
    Linear: 0% -> 1.0, 100% -> 6.0. Ergebnis auf `round_to` runden (z.B. 0.1).
    """
    try:
        p = float(percent)
    except (TypeError, ValueError):
        raise ValueError("percent muss eine Zahl sein")
    p = _clamp(p, 0.0, 100.0)
    grade = 1.0 + (p / 100.0) * 5.0
    if round_to:
        factor = 1.0 / float(round_to)
        grade = round(grade * factor) / factor
    return _clamp(grade, 1.0, 6.0)

def weighted_average(grades, weights=None, round_to=0.1):
    """
    Berechnet gewichteten Durchschnitt aus Schweizer Noten (1.0-6.0).
    grades: Liste von Zahlen (z.B. [5.5, 4.0, 6.0])
    weights: Liste gleicher Länge oder None (dann gleiche Gewichte).
    Ergebnis gerundet auf `round_to`.
    """
    if not grades:
        raise ValueError("grades-Liste darf nicht leer sein")
    g = [float(x) for x in grades]
    if weights is None:
        w = [1.0] * len(g)
    else:
        if len(weights) != len(g):
            raise ValueError("weights muss die gleiche Länge wie grades haben")
        w = [float(x) for x in weights]
    total_w = sum(w)
    if total_w == 0:
        raise ValueError("Summe der Gewichte darf nicht 0 sein")
    mean = sum(gi * wi for gi, wi in zip(g, w)) / total_w
    if round_to:
        factor = 1.0 / float(round_to)
        mean = round(mean * factor) / factor
    return _clamp(mean, 1.0, 6.0)

def notenberechner_interactive():
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
        ws = input("Gewichte eingeben (optional, gleiche Anzahl), getrennt durch Leerzeichen, oder Enter für gleiche Gewichte: ").strip()
        try:
            if ws:
                weights = ws.split()
                result = weighted_average(gs, weights)
            else:
                result = weighted_average(gs, None)
            print(f"Gewichteter Durchschnitt: {result:.1f}")
        except ValueError as e:
            print("Fehler:", e)
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    notenberechner_interactive()
