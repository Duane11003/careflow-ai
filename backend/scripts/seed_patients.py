
from collections.abc import Callable
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.patient import Patient


def seed_patients(
    session_factory: Callable[[], Session] = SessionLocal,
) -> None:
    patients = [
        Patient(
            first_name="John",
            last_name="Smith",
            discharge_date=date(2026, 6, 28),
            follow_up_status="pending",
        ),
        Patient(
            first_name="Jane",
            last_name="Smith",
            discharge_date=date(2026, 10, 28),
            follow_up_status="pending",
        ),
        Patient(
            first_name="Adam",
            last_name="Smith",
            discharge_date=date(2026, 7, 28),
            follow_up_status="pending",
        ),
    ]

    with session_factory() as db:
        for patient in patients:
            statement = select(Patient).where(
                Patient.first_name == patient.first_name,
                Patient.last_name == patient.last_name,
                Patient.discharge_date == patient.discharge_date,
            )

            existing_patient = db.scalar(statement)

            if existing_patient is None:
                db.add(patient)

        db.commit()


if __name__ == "__main__":
    seed_patients()
