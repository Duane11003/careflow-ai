from app.schemas.patient import Patient
from app.services.patient_service import get_all_patients, get_patient_by_id
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get('/api/patients', response_model=list[Patient])
def return_patients():
    return get_all_patients()


@router.get('/api/patients/{patient_id}', response_model=Patient)
def return_patient(patient_id: int):
    patient = get_patient_by_id(patient_id)
   
    if patient:
        return patient

    raise HTTPException(
        status_code=404,
        detail=f"No patient found for {patient_id}"
    )