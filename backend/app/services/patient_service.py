from app.schemas.patient import Patient
from datetime import date

patient_one = Patient(id=1, first_name="John", last_name="Smith", discharge_date=date(2026, 6, 28), follow_up_status="Completed")
patient_two = Patient(id=2, first_name="Jane", last_name="Smith", discharge_date=date(2026, 10, 28), follow_up_status="Pending")
patient_three = Patient(id=3, first_name="Adam", last_name="Smith", discharge_date=date(2026, 7, 28), follow_up_status="Pending")

patients_list = [patient_one, patient_two, patient_three]

def get_all_patients() -> list[Patient]:
    return patients_list

def get_patient_by_id(patient_id: int) -> Patient | None: 
     patient = next((p for p in patients_list if p.id == patient_id), None) # find the first patient with the matching ID, or return None
     return patient