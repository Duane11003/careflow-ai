from sqlalchemy.orm import Session

from app.services.patient_service import get_all_patients, get_patient_by_id


def test_get_all_patients(db_session: Session):
    patients = get_all_patients(db_session)

    assert len(patients) == 3


def test_get_patient_by_id(db_session: Session):
    patient = get_patient_by_id(db_session, 1)

    assert patient is not None
    assert patient.id == 1
    assert patient.first_name == "John"


def test_get_patient_by_id_not_found(db_session: Session):
    patient = get_patient_by_id(db_session, 100)

    assert patient is None