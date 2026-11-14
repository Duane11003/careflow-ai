
from datetime import date

from sqlalchemy import select

from app.database import SessionLocal
from app.models.appointment import Appointment
from app.models.patient import Patient
from app.models.medication import Medication

from typing import TypedDict

class AppointmentSeed(TypedDict):
    patient: tuple[str, str]
    date: date
    provider: str
    reason: str
    status: str


def seed_appointments() -> None:
    appointments: list[AppointmentSeed] = [
        {
            "patient": ("John", "Smith"),
            "date": date(2026, 12, 1),
            "provider": "Dr. Williams",
            "reason": "Blood pressure follow-up",
            "status": "scheduled",
        },
        {
            "patient": ("Jane", "Smith"),
            "date": date(2026, 12, 3),
            "provider": "Dr. Patel",
            "reason": "Cholesterol review",
            "status": "scheduled",
        },
        {
            "patient": ("Adam", "Smith"),
            "date": date(2026, 12, 5),
            "provider": "Dr. Chen",
            "reason": "Medication review",
            "status": "scheduled",
        },
    ]

    with SessionLocal() as db:
        for item in appointments:
            first_name, last_name = item["patient"]

            patient = db.scalars(
                select(Patient).where(
                    Patient.first_name == first_name,
                    Patient.last_name == last_name,
                )
            ).first()

            if patient is None:
                raise ValueError(
                    f"Patient {first_name} {last_name} not found"
                )

            existing_appointment = db.scalars(
                select(Appointment).where(
                    Appointment.patient_id == patient.id,
                    Appointment.date == item["date"],
                    Appointment.provider == item["provider"],
                    Appointment.reason == item["reason"],
                )
            ).first()

            if existing_appointment is None:
                db.add(
                    Appointment(
                        patient_id=patient.id,
                        date=item["date"],
                        provider=item["provider"],
                        reason=item["reason"],
                        status=item["status"],
                    )
                )

        db.commit()


if __name__ == "__main__":
    seed_appointments()
