from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel
from datetime import datetime
from src.Controller import AirLineController 

router = APIRouter(
    prefix="/api/flight",
)

@router.get("/search/all")
async def search_all():
    controller = AirLineController.AirLineController()
    found_flights = controller.search_all()
    if not found_flights:
        raise HTTPException(status_code=404, detail="No flights found for the given criteria")
    return found_flights

@router.get("/search/one-way/{departure_airport}/{destination_airport}/{departure_date}")
async def search_flight(departure_airport: str ,destination_airport:str ,departure_date: str):

    controller = AirLineController.AirLineController()  
    found_flights = controller.search_one_way(departure_airport, destination_airport, departure_date)
    if not found_flights:
        raise HTTPException(status_code=404, detail="No flights found for the given criteria")
    return found_flights