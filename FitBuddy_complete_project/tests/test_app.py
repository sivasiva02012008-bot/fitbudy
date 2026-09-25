from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert "FitBuddy" in r.text

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_dashboard():
    r = client.get("/view-all-users")
    assert r.status_code == 200
    assert "All Users" in r.text
