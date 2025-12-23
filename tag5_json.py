import json
from pathlib import Path



DATA_FILE = Path("patients.json")


def save_patients(patients: list[dict]) -> None:
    """Speichert Patienten als JSON-Datei."""
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(patients, f, ensure_ascii=False, indent=2)


def load_patients() -> list[dict]:
    """Lädt Patienten aus JSON-Datei. Gibt leere Liste zurück, wenn Datei fehlt."""
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def ensure_patient_ids(patients: list[dict]) -> list[dict]:
    """Vergibt IDs nachträglich, falls sie fehlen."""
    next_id = 1
    for patient in patients:
        if "id" not in patient:
            patient["id"] = next_id
            next_id += 1
        else:
            next_id = max(next_id, patient["id"] + 1)
    return patients


def get_next_id(patients: list[dict]) -> int:
    """Ermittelt die nächste freie Patienten-ID."""
    if not patients:
        return 1
    return max(p["id"] for p in patients) + 1


def main():
    # 1) Patienten laden + IDs sicherstellen
    patients = load_patients()
    patients = ensure_patient_ids(patients)

    # 2) Eingaben
    name = input("Name des Patienten: ").strip()
    if not name:
        print("❌ Name darf nicht leer sein.")
        return

    age_text = input("Alter: ").strip()
    if not age_text.isdigit():
        print("❌ Alter muss eine Zahl sein.")
        return
    age = int(age_text)

    mood = input("Stimmung (z.B. gut, müde, gestresst): ").strip()
    if not mood:
        mood = "unbekannt"

    # 3) Neue ID + Patient erzeugen
    new_id = get_next_id(patients)
    new_patient = {
        "id": new_id,
        "name": name,
        "age": age,
        "mood": mood,
    }

    # 4) Anhängen + speichern
    patients.append(new_patient)
    save_patients(patients)

    print("✅ Neuer Patient gespeichert.")

    # 5) Ausgabe
    print("📋 Aktuelle Patientenliste:")
    for p in patients:
        print(f"- [{p['id']}] {p['name']}")


if __name__ == "__main__":
    main()