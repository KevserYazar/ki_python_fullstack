from pydantic import BaseModel
from fastapi import FastAPI
from pathlib import Path
import json
from fastapi import HTTPException

from tag5_json import ensure_patient_ids, get_next_id, save_patients


app = FastAPI(
    title="KI Python Fullstack API",
    version="0.1.0",
    description="Lernprojekt: Patientenliste als JSON über FastAPI"
)

DATA_FILE = Path("patients.json")
class PatientCreate(BaseModel):
    name: str
    age: int
    mood: str


def load_patients() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
def root():
    return {"status": "API läuft"}


@app.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    patients = load_patients()

    for patient in patients:
        if patient.get("id") == patient_id:
            return patient

    raise HTTPException(
        status_code=404,
        detail=f"Patient mit ID {patient_id} nicht gefunden"
    )

@app.post("/patients")
def create_patient(patient: PatientCreate):
    patients = load_patients()

    # IDs sicherstellen (für alte Daten)
    patients = ensure_patient_ids(patients)

    # neue ID vergeben
    new_id = get_next_id(patients)

    new_patient = {
        "id": new_id,
        "name": patient.name,
        "age": patient.age,
        "mood": patient.mood,
    }

    patients.append(new_patient)
    save_patients(patients)

    return new_patient

#============================================================================

"Erklärungen"
# app= FastAPI(): Erstellt meinen Server
# @app.get("/patients"): Definiert eine API-Route, Endbpunkt

#patients/{patient_id} bedeutet:
#{patient_id} = Variable in der URL
#FastAPI wandelt automatisch in int

# HTTPException
#Richtiger HTTP-Fehler
#Kunden & Frontends erwarten das



#Bedeutet: Wenn jemand  "/patients" aufruft → führe diese Funktion aus
# load_patients(): Lädt Patientendaten aus einer JSON-Datei
# return patients: FAstApi gibt die Patientendaten automatisch als JSON-Antwort zurück
"API starten"
#Im Terminal (Projektordner, .venv aktiv): im bash eingeben = "uvicorn api:app --reload"
#uvicorn api:app --reload
#uvicorn = Server, Uvicorn lädt exakt das, was du angibst:
#bedeutet: Datei: api.py
#.        Variable: app 
"Ein Backend läuft dauerhaft."
#Ein Backend läuft dauerhaft.
#Man startet es nicht jedes Mal neu,
#sondern greift einfach darauf zu.