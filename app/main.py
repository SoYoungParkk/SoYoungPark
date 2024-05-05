from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/location", response_class=HTMLResponse)
def get_location_form():
    form = """
    <form method="post">
    <label for="location">지역 입력:</label><br>
    <input type="text" id="location" name="location" required><br>
    <button type="submit">확인</button>
    </form>
    """
    return form

@app.post("/location")
def receive_location(location: str = Form(...)):
    return {"입력받은 지역": location}
