# https://www.youtube.com/watch?v=Dnp07ZKfdVU&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=4
# python -m uvicorn Example_4:app --reload
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

# http://127.0.0.1:8000/bands
# http://127.0.0.1:8000/bands?genre=rock
# http://127.0.0.1:8000/bands?has_albums=true
# http://127.0.0.1:8000/bands?genre=metal&has_albums=true | http://127.0.0.1:8000/bands?genre=rock&has_albums=true
@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[Band]:
	bands_list = []
	# BOTH genre and has_albums query is provided
	if genre and has_albums == True:
		for b in BANDS_OBJ:
			if b.genre.lower() == genre.value.lower() and len(b.albums) > 0:
				bands_list.append(b)
		return bands_list
	# ONLY genre query paramater is provided
	elif genre:
		for b in BANDS_OBJ:
			if b.genre.lower() == genre.value.lower():
				bands_list.append(b)
		return bands_list
	# ONLY has_albums query paramater is provided
	elif has_albums == True:
		for b in BANDS_OBJ:
			if len(b.albums) > 0:
				bands_list.append(b)
		return bands_list
	# no query url return all bands
	else:
		return BANDS_OBJ

@app.get('/bands/{band_id}')
async def band(band_id: int) -> Band:
	# search for band id
	for b in BANDS_OBJ:
		if b.id == band_id:
			return b
	# handle exception if the band is not found
	raise HTTPException(status_code=404, detail='Band not found')