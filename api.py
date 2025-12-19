from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PatientData(BaseModel):
    age: int
    risk: str


@app.get("/")
def health_check():
    return {"status": "API läuft 🚀"}

# ===========================================================================
# API Endpunkte:
# http://127.0.0.1:8000 - Root-Endpunkt
# http://127.0.0.1:8000/docs - Automatische API-Dokumentation (Swagger UI)
# http://127.0.0.1:8000/risk?age=72 - Risiko-Check
# http://127.0.0.1:8000/patient - POST für Patientendaten
# ===========================================================================

def check_risk(age: int) -> str:
    if age > 60:
        return "hoch"
    return "normal"

@app.get("/risk")
def get_risk(age: int):
    return {
        "age": age,
        "risk": check_risk(age)
    }


@app.post("/patient")
async def analyze_patient(patient: PatientData):
    """Analysiert Patientendaten und gibt Empfehlungen zurück"""
    risk_level = check_risk(patient.age)
    
    recommendation = ""
    if risk_level == "hoch":
        recommendation = "Regelmäßige Kontrollen empfohlen"
    else:
        recommendation = "Normale Vorsorgeuntersuchungen ausreichend"
    
    return {
        "age": patient.age,
        "submitted_risk": patient.risk,
        "calculated_risk": risk_level,
        "recommendation": recommendation,
        "match": patient.risk == risk_level
    }

#Browser öffnen:
#http://127.0.0.1:8000/risk?age=72
{
  "age": 72,
  "risk": "hoch"
}
#========================================================================== 
