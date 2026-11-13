
from sqlalchemy import select

from app.database import SessionLocal
from app.models.medication import Medication
from app.models.patient import Patient


def seed_medications() -> None:
    medications = [
        {
            "patient": ("John", "Smith"),
            "name": "Lisinopril",
            "dosage": "10 mg",
            "frequency": "Once daily",
        },
        {
            "patient": ("John", "Smith"),
            "name": "Metformin",
            "dosage": "500 mg",
            "frequency": "Twice daily",
        },
        {
            "patient": ("Jane", "Smith"),
            "name": "Atorvastatin",
            "dosage": "20 mg",
            "frequency": "Once daily",
        },
        {
            "patient": ("Adam", "Smith"),
            "name": "Amlodipine",
            "dosage": "5 mg",
            "frequency": "Once daily",
        },
    ]

    with SessionLocal() as db:
        for item in medications:
            first_name, last_name = item["patient"]

            # Find the patient in PostgreSQL
            patient = db.scalar(
                select(Patient).where(
                    Patient.first_name == first_name,
                    Patient.last_name == last_name,
                )
            )

            if patient is None:
                raise ValueError(
                    f"Patient {first_name} {last_name} not found"
                )

            # Check whether the medication already exists
            existing_medication = db.scalar(
                select(Medication).where(
                    Medication.patient_id == patient.id,
                    Medication.name == item["name"],
                    Medication.dosage == item["dosage"],
                    Medication.frequency == item["frequency"],
                )
            )

            if existing_medication is None:
                medication = Medication(
                    patient_id=patient.id,
                    name=item["name"],
                    dosage=item["dosage"],
                    frequency=item["frequency"],
                )

                db.add(medication)

        db.commit()


if __name__ == "__main__":
    seed_medications()
