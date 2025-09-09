# https://www.youtube.com/watch?v=9Hc-mql6Gv4&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=6
# python -m uvicorn Example_6:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI, HTTPException, Path, Query
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID
from typing import Annotated

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
# http://127.0.0.1:8000/bands?genre=rock&q=Blac
# http://127.0.0.1:8000/bands?genre=rock
# http://127.0.0.1:8000/bands?q=Blac
# http://127.0.0.1:8000/bands?genre=rock&q=Blacccccccccccccccccccccccc
@app.get('/bands')
async def bands(
	genre: GenreURLChoices | None = None,
	q: Annotated[str | None, Query(max_length=10)] = None
) -> list[BandWithID]:
	bands_list = []
	#
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

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
	id = BANDS[-1]['id'] + 1
	# model dump will conver the pydantic object into a python dictionary
	band = BandWithID(id=id, **band_data.model_dump()).model_dump()
	BANDS.append(band)

	BANDS_OBJ = band_list_to_object(BANDS)

	return band
