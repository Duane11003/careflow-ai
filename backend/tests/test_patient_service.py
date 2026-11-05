from app.services.patient_service import get_all_patients, get_patient_by_id
from app.schemas.patient import Patient

def test_get_all_patients():
    patients = get_all_patients()

    assert isinstance(patients, list)
    assert len(patients) == 3
    assert all(isinstance(patient, Patient) for patient in patients)


def test_get_patient_by_id():
    patient = get_patient_by_id(1)

    assert isinstance(patient, Patient)
    assert patient.id == 1
    assert patient.first_name == "John"

def test_get_patient_by_id_not_found():
    patient = get_patient_by_id(100)

    assert patient is None