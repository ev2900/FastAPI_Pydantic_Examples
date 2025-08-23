# https://www.youtube.com/watch?v=zq0_g3BKltE&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=5
# python -m uvicorn Example_5:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID

app = FastAPI()

# Create a BANDS dictonary to acts as a fake database
BANDS = [
	{'id':1, 'name':'The Kinks', 'genre':'Rock'},
	{'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
	{'id':3, 'name':'Black Sabbath', 'genre':'Metal', 'albums': [{'title':'Master of Reality', 'release_date':'1971-07-21'}]},
	{'id':4, 'name':'Wu-Tang Clan', 'genre':'Hip-Hop'}
]

# Convert the BANDS dictonary into a list of Pydantic model instances of Band() 
def band_list_to_object(band_list):
	BANDS_OBJECTS = []
	for b in band_list:
		band = BandWithID(**b)
		BANDS_OBJECTS.append(band)
	return BANDS_OBJECTS

BANDS_OBJ = band_list_to_object(BANDS)

# HTTP routes / APIs

# http://127.0.0.1:8000/bands
# http://127.0.0.1:8000/bands?genre=rock
# http://127.0.0.1:8000/bands?has_albums=true
# http://127.0.0.1:8000/bands?genre=metal&has_albums=true | http://127.0.0.1:8000/bands?genre=rock&has_albums=true
@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[BandWithID]:
	bands_list = []
	# BOTH genre and has_albums query is provided
	if genre and has_albums == True:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if b.genre.lower() == genre.value.lower() and len(b.albums) > 0:
				bands_list.append(b)
		return bands_list
	# ONLY genre query paramater is provided
	elif genre:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if b.genre.lower() == genre.value.lower():
				bands_list.append(b)
		return bands_list
	# ONLY has_albums query paramater is provided
	elif has_albums == True:
		BANDS_OBJ = band_list_to_object(BANDS)
		for b in BANDS_OBJ:
			if len(b.albums) > 0:
				bands_list.append(b)
		return bands_list
	# no query url return all bands
	else:
		BANDS_OBJ = band_list_to_object(BANDS)
		return BANDS_OBJ

@app.get('/bands/{band_id}')
async def band(band_id: int) -> BandWithID:
	# search for band id
	for b in BANDS_OBJ:
		if b.id == band_id:
			return b
	# handle exception if the band is not found
	raise HTTPException(status_code=404, detail='Band not found')

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
	id = BANDS[-1]['id'] + 1
	# model dump will conver the pydantic object into a python dictionary
	band = BandWithID(id=id, **band_data.model_dump()).model_dump()
	BANDS.append(band)

	BANDS_OBJ = band_list_to_object(BANDS)

	return band