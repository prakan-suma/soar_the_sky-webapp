import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.Controller import AirLineController
from src.Class import AirPlane, AirPort, FlightInstance, Flight
from datetime import datetime, timedelta


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

airline_controller = AirLineController.AirLineController()


def create_instance():
    with open('./src/database/flightInstances.json', "r") as f:
        flight_instances_json = json.load(f)

    with open('./src/database/airplane.json', "r") as f:
        airplane_json = json.load(f)

    # create airport
    with open('./src/database/airport.json', "r") as f:
        airport_json = json.load(f)

    airport_list = []
    airplane_list = []

    for airport in airport_json:
        airport_obj = AirPort.AirPort(
            airport['airport_id'], airport['airport_code'], airport['gate'], airport['name'], airport['location'])
        airport_list.append(airport_obj)

    for airplane in airplane_json:
        airplane_obj = AirPlane.AirPlane(
            airplane['airplane_id'], airplane['model'], airplane['capacity'], airplane['seat'])
        airplane_list.append(airplane_obj)

    # set airplane
    airline_controller.set_airplane_list(airplane_list)

    # set airport
    airline_controller.set_airport_list(airport_list)

    flight_instances_obj = []
    # create flight instance object\
    for flight_instance_list in flight_instances_json:
        for airports in airline_controller.get_airport_list():
            if airports.airport_id == flight_instance_list['departure_airport']:
                departure_airport = airports
            
            if airports.airport_id == flight_instance_list['destination_airport']:
                destination_airport = airports
            
        for airplanes in airline_controller.get_airplane_list():
            if airplanes.airplane_id == flight_instance_list['airplane']:
                airplane_id = airplanes
                
        flight_instance = FlightInstance.FlightInstance(flight_instance_list['flight_no'],departure_airport,destination_airport,flight_instance_list['departure_time'],flight_instance_list['arrival_time'],flight_instance_list['duration_time'],airplane_id,flight_instance_list['price'],flight_instance_list['departure_date'])
        
        flight_instances_obj.append(flight_instance)

    airline_controller.set_flight_instance(flight_instances_obj)

create_instance()


@app.get("/api/airport/search/all/")
async def get_airport_all():
    try:
        airport_list = [airport.to_dict()
                        for airport in airline_controller.get_airport_list()]
        return airport_list

    except Exception as e:

        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/flight/search/one-way/{passenger}/{departureAirport}/{destinationAirport}/{departureDate}/")
async def search_one_way(passenger, departureAirport, destinationAirport, departureDate):
    try:
        flight_found = [flights.to_dict() for flights in airline_controller.search_flight_one_way(
            departureAirport, destinationAirport, departureDate)]
        return flight_found

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/flight/search/round-trip/{passenger}/{departureAirport}/{destinationAirport}/{departureDate}/{returnDate}/")
async def search_one_way(passenger, departureAirport, destinationAirport, departureDate, returnDate):
    try:

        departure_flights, return_flights = airline_controller.search_flight_round_trip(
            departureAirport, destinationAirport, departureDate, returnDate)

        # Convert flights to dictionaries
        departure_flights = [flight.to_dict() for flight in departure_flights]
        return_flights = [flight.to_dict() for flight in return_flights]

        flight_found = {
            "departure_flights": departure_flights,
            "return_flights": return_flights
        }
        return flight_found

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
