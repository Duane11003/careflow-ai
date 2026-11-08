from app.schemas.patient import Patient
from app.services.patient_service import get_all_patients, get_patient_by_id
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from typing import Annotated

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