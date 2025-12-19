" Mood Evaluator - Ein einfaches Programm zur Stimmungsauswertung "

# Firmen nutzen Docstrings oft zur automatischen Generierung von API-Dokumentationen


def evaluate_mood(mood: str) -> str:
    """
    Bewertet die Stimmung basierend auf dem eingegebenen Text.

    Args:
        mood (str): Die Stimmung als Text (z.B. "glücklich", "traurig").

    Returns:
        str: Eine Bewertung der Stimmung ("positiv", "negativ", "neutral").
    """
    positive_moods = ["glücklich", "zufrieden", "aufgeregt","fröhlich","gut"]
    negative_moods = ["traurig", "wütend", "frustriert","deprimiert","schlecht"]

    mood = mood.lower().strip()

    if not mood:
        raise ValueError("Stimmung darf nicht leer sein")

    if mood in negative_moods:
        return "Das ist vollkommen okay. Sei sanft zu dir – Schritt für Schritt wird es besser 💙"

    if mood in positive_moods:
        return "Das ist großartig! Behalte dieses Gefühl bei 💪✨"

    return "Danke, dass du deine Stimmung geteilt hast."

def main():
    try:
        mood = input("Wie fühlst du dich gerade? ")
        message = evaluate_mood(mood)
        print(message)
    except ValueError as error:
        print("Fehler:", error)


if __name__ == "__main__":
    main()
# ========================================================================