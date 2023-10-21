from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles




app = FastAPI()

@app.get("/user/id={id}")
async def get(id:int):
    print(id)
    return "chepuha"

app.mount("/", StaticFiles(directory="../public", html=True))

