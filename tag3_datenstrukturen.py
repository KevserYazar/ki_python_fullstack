#!/usr/bin/env python3
"""
Tag 3 — Datenstrukturen in Python - 
##Python Datenstrukturen & Logik (Grundlage jeder KI-Software)
### Das ist die Basis für APIs, KI-Pipelines, Datenverarbeitung, RAG, Agenten & Backends.

"""

# Alles, was du später baust:

## KI-Requests
## JSON-Antworten
## Datenbanken
## API-Payloads
## Embeddings
## RAG-Kontexte

# → besteht aus Listen, Dictionaries & Logik.

# ============================================================================
# 1. Listen (Lists)
# ============================================================================

## Listen sind geordnete, veränderbare Sammlungen von Elementen.
## Sie können Elemente hinzufügen, entfernen und ändern.
## Beispiel:

patients = ["Anna", "Max", "Lena"]

print(patients)
print(patients[0])      # erstes Element
print(len(patients))   # Anzahl der Elemente
patients.append("Tom")  # neues Element hinzufügen
print(patients)
patients.remove("Max") # Element entfernen
print(patients)
patients[1] = "Sophie" # Element ändern
print(patients)

# ============================================================================
# 2. Dictionaries (dict) – Schlüssel/Wert (SEHR wichtig)
# ============================================================================
# API-Antworten
# Patientendaten
# KI-Prompts
# JSON-Payloads
# Dictionaries sind ungeordnete, veränderbare Sammlungen von Schlüssel-Wert-Paaren.
# Sie ermöglichen den schnellen Zugriff auf Werte über ihre Schlüssel.
# Beispiel:

patient = {
    "name": "Sophie",
    "age": 34,
    "symptoms": ["Kopfschmerzen", "Müdigkeit"]
}

print(patient["name"])
print(patient["symptoms"])

patient["age"] = 35  # Wert ändern
print(patient)

# ============================================================================
# 3. Listen + Dictionaries kombinieren (realistische Anwendungsfälle)
# ==========================================================================
# Patientenliste mit Details
patients = [
    {
        "name": "Sophie",
        "age": 34,
        "symptoms": ["Kopfschmerzen"]
    },
    {
        "name": "Tom",
        "age": 41,
        "symptoms": ["Rückenschmerzen"]
    }
]

for patient in patients:
    print(patient["name"], "hat", patient["symptoms"])
# Neue Patientendaten hinzufügen    
new_patient = {
    "name": "Anna",
    "age": 29,
    "symptoms": ["Fieber"]
}
patients.append(new_patient)    
print(patients)
# Genau so sehen echte Daten in KI-Backends aus.


# ============================================================================
#4.Bedingungen (if / else) – Logik bauen
# ============================================================================
age = 20

if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")

def check_risk(age: int) -> str:
    if age > 60:
        return "Erhöhtes Risiko"
    else:
        return "Normales Risiko"

print(check_risk(72))
print(check_risk(45))

# ===========================================================================
#5. Schleifen (for) – Daten verarbeiten
# ===========================================================================
symptoms = ["Husten", "Fieber", "Kopfschmerzen"]

for symptom in symptoms:
    print("Symptom:", symptom)

# ===========================================================================
#6. Mini-Projekt (sehr wichtig!)

# Patientenliste verarbeiten und Risikobewertung ausgeben
# ===========================================================================
patients = [
    {"name": "Anna", "age": 34},
    {"name": "Max", "age": 68},
    {"name": "Lena", "age": 72},
]

for patient in patients:
    if patient["age"] > 60:
        print(patient["name"], "→ erhöhtes Risiko")
    else:
        print(patient["name"], "→ normales Risiko")

# So verarbeitest du echte Patientendaten in Backends & APIs.
#==========================================================
