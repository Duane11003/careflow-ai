from typing import Annotated

from app.database import get_db
from app.schemas.medication import Medication as MedicationSchema
from app.schemas.patient import Patient
from app.services.medication_service import get_medications_by_patient_id
from app.services.patient_service import get_all_patients, get_patient_by_id
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.appointment import Appointment as AppointmentSchema
from app.services.appointment_service import get_appointments_by_patient_id

router = APIRouter()


@router.get('/api/patients', response_model=list[Patient])
def get_patients(db: Annotated[Session, Depends(get_db)]):
    return get_all_patients(db)


@router.get('/api/patients/{patient_id}', response_model=Patient)
def get_patient(patient_id: int, db: Annotated[Session, Depends(get_db)]):
    patient = get_patient_by_id(db, patient_id)
    
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient

@router.get('/api/patients/{patient_id}/medications', response_model=list[MedicationSchema])
def get_patient_medications(patient_id: int, db: Annotated[Session, Depends(get_db)]):
    patient = get_patient_by_id(db, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return get_medications_by_patient_id(db, patient_id)

@router.get('/api/patients/{patient_id}/appointments', response_model=list[AppointmentSchema])
def get_patient_appointments(patient_id: int, db: Annotated[Session, Depends(get_db)]):
    patient = get_patient_by_id(db, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return get_appointments_by_patient_id(db, patient_id)