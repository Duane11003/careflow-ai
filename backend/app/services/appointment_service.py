from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.appointment import Appointment

def get_appointments_by_patient_id(db: Session, patient_id: int) -> list[Appointment]:
    statement = select(Appointment).where(Appointment.patient_id == patient_id)
    appointments = db.scalars(statement).all()
    return list(appointments)