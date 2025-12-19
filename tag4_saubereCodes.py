#!/usr/bin/env python3
#/Users/kevseryazar/ki_python_fullstack/.venv/bin/activate
"""
Tag 4 — Saubere Codes (Clean Code)
Best Practices für wartbaren, lesbaren und professionellen Python-Code

Warum Clean Code wichtig ist:
- Bessere Wartbarkeit
- Einfachere Zusammenarbeit im Team
- Weniger Bugs
- Schnellere Entwicklung auf lange Sicht
"""

# ============================================================================
# 1. Funktionen richtig denken und benennen 
# ============================================================================      
# ============================================================================  
 
### Unsauber (Anfänger-Stil):
age = 72
if age > 60:
    print("hoch")
else:
    print("normal")
# Unsauber: Keine Funktionen, keine Struktur
# Schwer zu lesen und wiederzuverwenden 

### Sauber (Profi-Stil):
def evaluate_risk(age: int) -> str:
    return "hoch" if age > 60 else "normal"
# Sauber: Klare Funktion mit einem Zweck
# Leicht zu lesen, zu testen und wiederzuverwenden



#Eine Funktion = eine Verantwortung


# ============================================================================
# 2. Typannotationen (extrem wichtig für KI & APIs)
# ============================================================================  

def evaluate_risk_v1(age: int) -> str:
    return "hoch" if age > 60 else "normal" 


# Typannotationen helfen bei der Lesbarkeit und Fehlervermeidung    
# Sie sind besonders wichtig bei der Arbeit mit KI-Modellen und APIs
# Sie ermöglichen bessere Autovervollständigung und Fehlerprüfung in IDEs

# ========================================================================



# 3.Trennung von Logik & Ausführung 
# ============================================================================  
### Profi-Struktur:
def  evaluate_risk_v2(age: int) -> str:
    return "hoch" if age > 60 else "normal"

def main_example():
    age = int(input("Alter: "))
    print(evaluate_risk_v2(age))

#if __name__ == "__main__":
#    main_example()


# Trennung von Logik (evaluate_risk) und Ausführung (main)
# Erleichtert Tests und Wiederverwendung des Codes
# Vorbereitung für APIs & Tests
# ================================================================================================================  


# 4.Docstrings – dein Code erklärt sich selbst
# ============================================================================


def evaluate_risk_v3(age: int) -> str:
    """
    Bewertet das Risiko basierend auf dem Alter.

    Args:
        age (int): Alter der Person

    Returns:
        str: "hoch" oder "normal"
    """
   
    return "hoch" if age > 60 else "normal"

# Docstrings sind wichtig für die Dokumentation
# Sie helfen anderen (und dir selbst), den Code später zu verstehen
# Besonders wichtig bei der Arbeit in Teams und mit APIs
# Firmen nutzen Docstrings oft zur automatischen Generierung von API-Dokumentationen
# Firmen lieben sauberen Code mit Docstrings

# ============================================================================  


# 5.Fehler bewusst behandeln (Backend-Denken)
# ===========================================================================

def evaluate_risk_v4(age: int) -> str:
    if age < 0:
        raise ValueError("Alter darf nicht negativ sein")
    return "hoch" if age > 60 else "normal"
# Fehlerbehandlung ist ein wichtiger Teil von sauberem Code
# Sie sorgt dafür, dass dein Programm robust und benutzerfreundlich ist
# Besonders wichtig bei der Arbeit mit APIs, wo viele unerwartete Eingaben auftreten können 

#===========================================================================


#6.Mini-Refactoring (wichtig!)
# ===========================================================================

patients = [
    {"name": "Anna", "age": 34},
    {"name": "Max", "age": 72}
]

for p in patients:
    if p["age"] > 60:
        print(p["name"], "hoch")
    else:
        print(p["name"], "normal")
# Refactoring: Code verbessern, ohne sein Verhalten zu ändern
# Macht den Code lesbarer und wartbarer
# Wichtig für die langfristige Pflege von Projekten

def evaluate_risk_(age: int) -> str:
    return "hoch" if age > 60 else "normal"

def evaluate_patients(patients: list[dict]) -> list[dict]:
    results = []
    for patient in patients:
        results.append({
            "name": patient["name"],
            "risk": evaluate_risk_(patient["age"])
        })
    return results

def main():
    patients = [
        {"name": "Anna", "age": 34},
        {"name": "Max", "age": 72}
    ]
    print(evaluate_patients(patients))

if __name__ == "__main__":
    main()

#===========================================================================
# Ende des sauberen Codes
#===========================================================================

#Denkweise: Vorbereitung auf FastAPI & KI-Modelle
 #FastAPI liest: Typen, Rückgabewerte und Docstrings
    #KI-Modelle lesen: klare Strukturen

# und baut daraus: API-Dokumentation, Validierung, klare Fehler
    # und bessere Zusammenarbeit im Team
# ============================================================================