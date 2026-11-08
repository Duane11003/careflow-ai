from datetime import date

from app.database import SessionLocal
from app.models.patient import Patient

db = SessionLocal()

patient = Patient(
    first_name="John",
    last_name="Smith",
    discharge_date=date(2026, 6, 28),
    follow_up_status="pending"
)

try:
    db.add(patient)
    db.commit()
finally:
    db.close()