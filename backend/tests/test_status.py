from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_status_endpoint_returns_running():
    response = client.get("/api/status")
    assert response.status_code == 200
    body = response.json()
    assert body.get("status") == "running"


