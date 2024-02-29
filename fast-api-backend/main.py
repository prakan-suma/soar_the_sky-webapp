# uvicorn main:app --reload
from fastapi import FastAPI
from routers import flights as flights


app = FastAPI()

@app.get("/")
async def root():
    return "back-end"

app.include_router(flights.router)

