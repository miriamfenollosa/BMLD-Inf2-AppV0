import datetime

def berechne_note(punkte, max_punkte):
    if max_punkte == 0:
        return {"note": None, "timestamp": datetime.datetime.now()}
    prozent = (punkte / max_punkte) * 5 + 1
    note = round(prozent, 1)
    return {"note": note, "timestamp": datetime.datetime.now()}
