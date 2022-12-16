from fastapi import FastAPI
from countryinfo import CountryInfo

app = FastAPI()

@app.get("/")
async def get_country(country:str):
    co = CountryInfo(country).info()
    return co