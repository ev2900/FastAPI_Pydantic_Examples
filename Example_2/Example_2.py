# https://www.youtube.com/watch?v=q6E3xoKIBnY&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=2
# python -m uvicorn Example_2:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop' 

BANDS = [
	{'id':1, 'name':'The Kinks', 'genre':'Rock'},
	{'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
	{'id':3, 'name':'Slowdive', 'genre':'Shoegaze'},
	{'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-hop'}
]

@app.get('/bands')
async def bands() -> list[dict]:
	return BANDS

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
	# search for band id
	for b in BANDS:
		if b['id'] == band_id:
			return b
	# handle exception if the band is not found
	raise HTTPException(status_code=404, detail='Band not found')

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
	# search for bands that match the searched for genre
	r = []
	for b in BANDS:
		if b['genre'].lower() == genre.value:
			r.append(b)
	return r