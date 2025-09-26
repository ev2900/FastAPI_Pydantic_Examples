# https://www.youtube.com/watch?v=9Hc-mql6Gv4&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=8
# python -m uvicorn Example_7:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoices, BandCreate, Band, Album
from typing import Annotated
from contextlib import asynccontextmanager
from db import init_db, get_session

# code to run before FastAPI starts ie. start the database
@asynccontextmanager
async def lifespan(app: FastAPI):
	init_db()
	yield

app = FastAPI(lifespan = lifespan)

# Create a BANDS dictonary to acts as a fake database
BANDS = [
	{'id':1, 'name':'The Kinks', 'genre':'Rock'},
	{'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
	{'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]},
	{'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-Hop'}
]

'''
# Convert the BANDS dictonary into a list of Pydantic model instances of Band() 
def band_list_to_object(band_list):
	BANDS_OBJECTS = []
	for b in band_list:
		band = BandWithID(**b)
		BANDS_OBJECTS.append(band)
	return BANDS_OBJECTS

BANDS_OBJ = band_list_to_object(BANDS)

# HTTP routes / APIs
@app.get('/bands')
async def bands(
	genre: GenreURLChoices | None = None,
	q: Annotated[str | None, Query(max_length=10)] = None
) -> list[BandWithID]:

	bands_list = []
	# genre query paramater and query paramater q is provided, see if q is in the name of the band, like a search
	if genre and q == True:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if (b.genre.value.lower() == genre.value.lower()) and (q.lower() in b.name.lower()):
				bands_list.append(b)
		return bands_list

	# genre query paramater is provided
	elif genre:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if b.genre.value.lower() == genre.value.lower():
				bands_list.append(b)
		return bands_list
	# if query paramater q is provided, see if q is in the name of the band, like a search
	elif q:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if q.lower() in b.name.lower():
				bands_list.append(b)
		return bands_list
	# no query url return all bands
	else:
		BANDS_OBJ = band_list_to_object(BANDS)
		return BANDS_OBJ

@app.get('/bands/{band_id}')
async def band(band_id: Annotated[int, Path(title="The band ID")]) -> BandWithID: # the annotated title will show up in the /docs
	# search for band id
	for b in BANDS_OBJ:
		if b.id == band_id:
			return b
	# handle exception if the band is not found
	raise HTTPException(status_code=404, detail='Band not found')
'''

@app.post('/bands')
async def create_band(band_data: BandCreate) -> Band:
	band = Band(name = band_data.name, genre = band_data.genre)


	return band