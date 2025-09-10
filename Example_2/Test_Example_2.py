# Unit tests for Example_2.py
# python -m pytest

from fastapi.testclient import TestClient
from Example_2 import app

client = TestClient(app)

# /bands
def test_bands():
	response = client.get("/bands")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock'}, {'id':2, 'name':'Aphex Twin', 'genre':'Electronic'}, {'id':3, 'name':'Slowdive', 'genre':'Shoegaze'}, {'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-hop'}]

# /bands/{band_id}
def test_bands_id():
	response = client.get("/bands/1")
	assert response.status_code == 200
	assert response.json() == {'id':1, 'name':'The Kinks', 'genre':'Rock'}

# /bands/genre/{genre}
def test_bands_genre():
	response = client.get("/bands/genre/rock")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock'}]