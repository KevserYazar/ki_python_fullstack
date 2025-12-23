from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI(
    title="KI Python Fullstack API",
    version="0.1.0",
    description="Lernprojekt: Patientenliste als JSON über FastAPI"
)

DATA_FILE = Path("patients.json")


def load_patients() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
def root():
    return {"status": "API läuft"}


@app.get("/patients")
def get_patients():
    return load_patients()

#============================================================================

"Erklärungen"
# app= FastAPI(): Erstellt meinen Server
# @app.get("/patients"): Definiert eine API-Route, Endbpunkt
#Bedeutet: Wenn jemand  "/patients" aufruft → führe diese Funktion aus
# load_patients(): Lädt Patientendaten aus einer JSON-Datei
# return patients: FAstApi gibt die Patientendaten automatisch als JSON-Antwort zurück
"API starten"
#Im Terminal (Projektordner, .venv aktiv): im bash eingeben = "uvicorn api:app --reload"
#uvicorn api:app --reload
#uvicorn = Server, Uvicorn lädt exakt das, was du angibst:
#bedeutet: Datei: api.py
#.        Variable: app 