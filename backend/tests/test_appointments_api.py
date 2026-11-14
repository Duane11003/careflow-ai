
from fastapi.testclient import TestClient


def test_get_patient_appointments_success(client: TestClient):
    response = client.get("/api/patients/1/appointments")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["patient_id"] == 1
    assert data[0]["provider"] == "Dr. Williams"
    assert data[0]["status"] == "scheduled"


def test_get_patient_appointments_empty(client: TestClient):
    response = client.get("/api/patients/2/appointments")

    assert response.status_code == 200
    assert response.json() == []


def test_get_patient_appointments_not_found(client: TestClient):
    response = client.get("/api/patients/999/appointments")

    assert response.status_code == 404
    assert response.json()["detail"] == "Patient not found"
