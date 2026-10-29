from fastapi import APIRouter
from app.schemas.patient import Patient
from datetime import date

router = APIRouter()

patient_one = Patient(id=1, first_name="John", last_name="Smith", discharge_date=date(2026, 6, 28), follow_up_status="pending")
patient_two = Patient(id=2, first_name="Jane", last_name="Smith", discharge_date=date(2026, 10, 28), follow_up_status="pending")
patient_three = Patient(id=3, first_name="Adam", last_name="Smith", discharge_date=date(2026, 7, 28), follow_up_status="pending")

patients_list = [patient_one, patient_two, patient_three]

@router.get('/api/patients')
def return_patients():
    return patients_list


