from fastapi import FastAPI
import services as service

app = FastAPI()

@app.get("/scraper")
async def main_scraper():
    return service.get_all_autos()
