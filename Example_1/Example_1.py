# https://www.youtube.com/watch?v=Lw-zLopB3o0&list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY&index=2
# python -m uvicorn Example_1:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index() -> dict[str, str]:
	return {"hello":"world"}

@app.get('/about')
async def about() -> str:
	return 'An Exceptional Company'