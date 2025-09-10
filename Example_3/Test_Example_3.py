# Unit tests for Example_3.py
# python -m pytest

from fastapi.testclient import TestClient
from Example_3 import app

client = TestClient(app)

# /bands
def test_bands():
	response = client.get("/bands")
	assert response.status_code == 200
	assert response.json() ==  [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': []}, {'id':2, 'name':'Aphex Twin', 'genre':'Electronic', 'albums': []}, {'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]}, {'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-hop', 'albums': []}]

# /bands/{band_id}
def test_bands_id():
	response = client.get("/bands/1")
	assert response.status_code == 200
	assert response.json() == {'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': []}

# /bands/genre/{genre}
def test_bands_genre():
	response = client.get("/bands/genre/rock")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock'}]