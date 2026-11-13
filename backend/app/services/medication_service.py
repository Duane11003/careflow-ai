from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.medication import Medication

def get_medications_by_patient_id(db: Session, patient_id: int) -> list[Medication]:
    statement = select(Medication).where(Medication.patient_id == patient_id)
    medications = db.scalars(statement).all()
    return list(medications)