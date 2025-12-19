'Anforderungen:'

# Liste mit mindestens 3 Personen
#Jede Person:
##Name
##Alter
##Stimmung (z.B. "glücklich", "traurig", "neutral")
# Das Programm soll:
  ## - jede Person ausgeben
  # ##- wenn Alter > 60 → Hinweis anzeigen
  # ##- sonst → motivierende Nachricht


patients = [
    {"name": "Hans", "age": 65, "mood": "glücklich"},
    {"name": "Clara", "age": 45, "mood": "neutral"},
    {"name": "Peter", "age": 70, "mood": "traurig"},
]
for patient in patients:
    name = patient["name"]
    age = patient["age"]
    mood = patient["mood"]  
    print(f"{name}, Alter: {age}, Stimmung: {mood}")
    if age > 60:
        print("Hinweis: Erhöhtes Risiko zur Depression aufgrund des Alters.")
    else:
        print("Bleib stark und positiv! Du schaffst das! 💪")
    print()  
    
# Beispielausgabe:
# Hans, Alter: 65, Stimmung: glücklich
# Hinweis: Erhöhtes Risiko zur Depression aufgrund des Alters.