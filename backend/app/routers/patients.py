from fastapi import APIRouter, HTTPException
from app.schemas.patient import Patient
from datetime import date

router = APIRouter()

patient_one = Patient(id=1, first_name="John", last_name="Smith", discharge_date=date(2026, 6, 28), follow_up_status="Completed")
patient_two = Patient(id=2, first_name="Jane", last_name="Smith", discharge_date=date(2026, 10, 28), follow_up_status="Pending")
patient_three = Patient(id=3, first_name="Adam", last_name="Smith", discharge_date=date(2026, 7, 28), follow_up_status="Pending")

patients_list = [patient_one, patient_two, patient_three]

@router.get('/api/patients', response_model=list[Patient])
def return_patients():
    return patients_list


@router.get('/api/patients/{patient_id}', response_model=Patient)
def return_patient(patient_id: int):
    patient = next((p for p in patients_list if p.id == patient_id), None) # find the first patient with the matching ID, or return None
    if patient:
        return patient

    raise HTTPException(
        status_code=404,
        detail=f"No patient found for {patient_id}"
    )