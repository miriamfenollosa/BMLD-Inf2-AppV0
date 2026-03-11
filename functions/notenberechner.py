import datetime

import pytz


def berechne_note(punkte, max_punkte):
    if max_punkte == 0:
        return "Maximale Punktzahl darf nicht 0 sein"
    
    prozent = (punkte / max_punkte) * 5 + 1

    return {
    "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
    "note": round(prozent, 1)
    }
