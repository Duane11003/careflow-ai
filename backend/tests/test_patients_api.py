from fastapi.testclient import TestClient

def test_get_patients_success(client: TestClient):
    response = client.get('/api/patients')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 3


def test_get_patient_by_id_success(client: TestClient):
    response = client.get('/api/patients/1')
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["first_name"] == "John"

def test_get_patient_by_id_failure(client: TestClient):
    response = client.get('/api/patients/999')
    data = response.json()
    assert response.status_code == 404
    assert data["detail"] == "Patient not found"