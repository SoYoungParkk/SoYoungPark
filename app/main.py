from fastapi import FastAPI # type: ignore

app = FastAPI()

hot_places = {
    "Seoul": [
        {"name": "Place 1", "latitude": 37.123, "longitude": 127.456},
        {"name": "Place 2", "latitude": 37.234, "longitude": 127.567},
        {"name": "Place 3", "latitude": 37.345, "longitude": 127.678},
    ],
    "Busan": [
        {"name": "Place A", "latitude": 35.234, "longitude": 129.345},
        {"name": "Place B", "latitude": 35.345, "longitude": 129.456},
        {"name": "Place C", "latitude": 35.456, "longitude": 129.567},
    ]
}

@app.get("/hot-places/{city}")
async def get_hot_places(city: str):
    return hot_places.get(city, [])
