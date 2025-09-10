# Unit tests for Example_4.py
# python -m pytest

from fastapi.testclient import TestClient
from Example_4 import app

client = TestClient(app)

# /bands
def test_bands():
	response = client.get("/bands")
	assert response.status_code == 200
	assert response.json() ==  [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': []}, {'id':2, 'name':'Aphex Twin', 'genre':'Electronic', 'albums': []}, {'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]}, {'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-hop', 'albums': []}]
	
# /bands?genre=rock
def test_bands_genre():
	response = client.get("/bands?genre=rock")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': []}]

# /bands?has_albums=true
def test_bands_has_albums():
	response = client.get("/bands?has_albums=true")
	assert response.status_code == 200
	assert response.json() == [{'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]}]

# /bands?genre=metal&has_albums=true
def test_bands_genre_has_albums():
	response = client.get("/bands?genre=metal&has_albums=true")
	assert response.status_code == 200
	assert response.json() == [{'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]}]