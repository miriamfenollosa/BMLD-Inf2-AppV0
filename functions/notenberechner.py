def berechne_note(punkte, max_punkte):
    if max_punkte == 0:
        return "Maximale Punktzahl darf nicht 0 sein"
    
    prozent = (punkte / max_punkte) * 5 + 1
    return round(prozent, 1)
