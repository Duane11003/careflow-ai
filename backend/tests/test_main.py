from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_return():
    response = client.get('/api/test')

    assert response.status_code == 200
    assert response.json() == 'test is working'



