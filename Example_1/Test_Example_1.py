# Unit tests for Example_1.py
# python -m pytest

from fastapi.testclient import TestClient
from Example_1 import app

client = TestClient(app)

# /
def test_root():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"hello":"world"}

# /about 
def test_about():
	response = client.get("/about")
	assert response.status_code == 200