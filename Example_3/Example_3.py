# https://www.youtube.com/watch?v=ID9b4diFZN8&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=3
# python -m uvicorn Example_3:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band

app = FastAPI()

# Create a BANDS dictonary to acts as a fake database
BANDS = [
	{'id':1, 'name':'The Kinks', 'genre':'Rock'},
	{'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
	{'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]},
	{'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-hop'}
]

# Convert the BANDS dictonary into a list of Pydantic model instances of Band() 
BANDS_OBJ = []
for b in BANDS:
	band = Band(**b)
	BANDS_OBJ.append(band)

# HTTP routes / APIs
@app.get('/bands')
async def bands() -> list[Band]:
	return BANDS_OBJ

@app.get('/bands/{band_id}')
async def band(band_id: int) -> Band:
	# search for band id
	for b in BANDS_OBJ:
		if b.id == band_id:
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