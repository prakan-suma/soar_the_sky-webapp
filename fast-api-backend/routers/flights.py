from fastapi import APIRouter, Depends, HTTPException
from src.Controller.AirLineController import AirLineController
from src.Class.FlightInstance import FlightInstance


router = APIRouter(
    prefix="/api/flight",
)

# Create a dependency to inject the airline_controller
def get_airline_controller():
    # Create and initialize the AirLineController instance here
    airline_controller = AirLineController.AirLineController()
    # Perform any necessary setup here
    return airline_controller

@router.get("/search/one-way/{passenger}/{departureAirport}/{destinationAirport}/{departureDate}/")
async def search_one_way(passenger, departureAirport, destinationAirport, departureDate, airline_controller: AirLineController = Depends(get_airline_controller)):
    # Now you can access airline_controller directly here
    # flight_found = [flight.to_dict() for flight in airline_controller.search_flight_one_way(departureAirport, destinationAirport, departureDate)]
    return airline_controller.get_airplane_list()