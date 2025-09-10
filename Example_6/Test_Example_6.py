# Unit tests for Example_6.py
# python -m pytest

from fastapi.testclient import TestClient
from Example_6 import app

client = TestClient(app)

# /bands
def test_bands():
	response = client.get("/bands")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums':[]}, {'id':2, 'name':'Aphex Twin', 'genre':'Electronic', 'albums':[]}, {'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]}, {'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-Hop', 'albums':[]}]

# bands?genre=rock&q=Blac
def test_bands_genre_q():
	response = client.get("/bands?genre=rock&q=Blac")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums':[]}]

# bands?genre=rock
def test_bands_genre():
	response = client.get("/bands?genre=rock")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums':[]}]

# bands?q=Blac
def test_bands_genre():
	response = client.get("/bands?q=Blac")
	assert response.status_code == 200
	assert response.json() == [{'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums':[]}]

# bands?genre=rock&q=Blacccccccccccccccccccccccc
def test_bands_genre():
	response = client.get("/bands?genre=rock&q=Blacccccccccccccccccccccccc")
	assert response.status_code == 422
	assert response.json() == {"detail":[{"type":"string_too_long","loc":["query","q"],"msg":"String should have at most 10 characters","input":"Blacccccccccccccccccccccccc","ctx":{"max_length":10}}]}

# /bands/{band_id}
def test_bands_id():
	response = client.get("/bands/1")
	assert response.status_code == 200
	assert response.json() == {'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': []}

# POST /bands
def test_bands_post():
	response = client.post("/bands", json = {"name": "Boards of Canada", "genre": "electronic", "albums": [{"title": "Tomorrow's Harvest","release_date": "2013-01-01"},{"title": "Music has the right to children", "release_date": "1998-01-01"}]})
	assert response.status_code == 200
	assert response.json() == {"name": "Boards of Canada", "genre": "Electronic", "albums": [{"title": "Tomorrow's Harvest", "release_date": "2013-01-01"}, {"title": "Music has the right to children", "release_date": "1998-01-01"}], "id": 5}