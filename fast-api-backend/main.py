import json
from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.Controller import AirLineController
from src.Class import AirPlane, AirPort, FlightInstance
from routers import flights


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# airline_controller instance
airline_controller = AirLineController.AirLineController()

# create airplane instance
airplane_list = AirPlane.AirPlane.create_instance()
airline_controller.set_airplane_list(airplane_list)

# create airport instance
airport_list = AirPort.AirPort.create_instance()
airline_controller.set_airport_list(airport_list)


# create departure flights isinstance
flight_list = [
    FlightInstance.FlightInstance("SDK212", "120", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        3), airline_controller.search_airplane_from_id("SA-3499-C"), 0, "2024-04-15", "2024-04-15", "06:00", "08:00", 1992),
    
    FlightInstance.FlightInstance("BKC928", "120", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        3), airline_controller.search_airplane_from_id("SA-3499-C"), 0, "2024-04-15", "2024-04-15", "10:00", "12:00", 2579),
    
    FlightInstance.FlightInstance("BL3928", "120", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        3), airline_controller.search_airplane_from_id("SA-3499-C"), 0, "2024-04-15", "2024-04-15", "14:00", "16:00", 2930),
    
    FlightInstance.FlightInstance("PKK938", "120", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        3), airline_controller.search_airplane_from_id("SA-3499-C"), 0, "2024-04-15", "2024-04-15", "17:00", "19:00", 2870),

    FlightInstance.FlightInstance("PSD352", "120", airline_controller.search_airport_from_id(3), airline_controller.search_airport_from_id(
        1), airline_controller.search_airplane_from_id("SA-3499-C"), None, "2024-04-18", "2024-04-18", "19:00", "21:00", 1834),

    FlightInstance.FlightInstance("KDC392", "120", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        3), airline_controller.search_airplane_from_id("S3-0320-C"), None, "2024-04-16", "2024-04-16", "10:00", "12:00", 2330),

    FlightInstance.FlightInstance("KFC007", "60", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        5), airline_controller.search_airplane_from_id("BA-EP33-C"), None, "2024-04-17", "2024-04-17", "10:00", "11:00", 1930),

    FlightInstance.FlightInstance("KFC007", "60", airline_controller.search_airport_from_id(1), airline_controller.search_airport_from_id(
        5), airline_controller.search_airplane_from_id("PW-7893-C"), None, "2024-04-17", "2024-04-17", "13:00", "14:00", 1288)
]

airline_controller.set_flight_instance(flight_list)

# Routes


@app.get("/api/airport/search/all/")
async def get_airport_all():
    try:
        airport_list = [airport.to_dict()
                        for airport in airline_controller.get_airport_list()]
        return airport_list

    except Exception as e:

        raise HTTPException(status_code=500, detail="Internal server error")

# search rount


@app.get("/api/flight/search/one-way/{passenger}/{departureAirport}/{destinationAirport}/{departureDate}/")
async def search_one_way(passenger, departureAirport, destinationAirport, departureDate):
    try:
        passenger = {"passenger": passenger}
        flight_found = [flights.to_dict() for flights in airline_controller.search_flight_one_way(
            departureAirport, destinationAirport, departureDate)]
        return  flight_found

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/flight/search/round-trip/{passenger}/{departureAirport}/{destinationAirport}/{departureDate}/{returnDate}/")
async def search_one_way(passenger, departureAirport, destinationAirport, departureDate, returnDate):
    try:
        # passenger = {"passenger": passenger}
        departure_flights, return_flights = airline_controller.search_flight_round_trip(
            departureAirport, destinationAirport, departureDate, returnDate)

        # Convert flights to dictionaries
        departure_flights = [flight.to_dict() for flight in departure_flights]

        return_flights = [flight.to_dict() for flight in return_flights]

        return {"departure_flights": departure_flights}, {"return_flights": return_flights}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
