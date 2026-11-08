
from app.models.patient import Patient
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_all_patients(db: Session) -> list[Patient]:
    statement = select(Patient)
    patients = db.scalars(statement).all()
    return list(patients)

def get_patient_by_id(db: Session, patient_id: int) -> Patient | None: 
    patient = db.get(Patient, patient_id)
    return patient