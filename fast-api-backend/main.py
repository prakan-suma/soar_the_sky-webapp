import json
import random
from fastapi import FastAPI, Body, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from src.Controller import AirLineController
from src.Class import AirPlane, AirPort, FlightInstance, Flight, User, Passenger, Booking, Payment, PaymentMethod, FlightSeat
from datetime import datetime, timedelta, date
from pydantic import BaseModel, ValidationError


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

airline_controller = AirLineController.AirLineController()


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

# user route


@app.post("/api/register/")
async def register(user_data: dict = Body(...)):
    try:
        username = user_data.get("username")
        password = user_data.get("password")
        confirm_password = user_data.get("confirm_password")
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        phone_number = user_data.get("phone_number")
        email = user_data.get("email")

        user_list = [
            user.username for user in airline_controller.get_user_list()]

        if password != confirm_password:
            return {"message": "Password not match!"}

        if username in user_list:
            return {"message": "This username is already taken."}

        user_count = len(airline_controller.get_user_list())
        new_user = User.User((user_count+1), username, password,
                             first_name, last_name, phone_number, email)

        new_user.add_user_to_json()

        return {"message": "User registered successfully!"}

    except ValidationError as e:
        # Return validation errors with status code 400 (Bad Request)
        return {"detail": e.errors()}, 400


@app.post("/api/login/")
async def login(user_data: dict = Body(...)):

    try:
        # Extract username and password from request body
        username = user_data.get("username")
        password = user_data.get("password")

        # Check for missing credentials
        if not username or not password:
            raise HTTPException(
                status_code=400, detail="Missing username or password")

        # Find user by username (implementation based on your user storage)
        user = None
        for user_obj in airline_controller.get_user_list():
            if user_obj.username == username:
                user = user_obj
                break

        # Check if user exists
        if not user:
            raise HTTPException(
                status_code=401, detail="Invalid username or password")

        # Validate password (plain text comparison for this example)
        if password != user.password:
            raise HTTPException(
                status_code=401, detail="Invalid username or password")

        # Login successful, generate a token
        return {"message": "Login successful!", "token": "<token>"}

    except Exception as e:
        return {"message": f"Login failed: {str(e)}"}, 500

# booking
# @app.post('/api/booking/payment/')
# async def booking_payment():
    


@app.post("/api/one-way/booking/")
async def one_way_booking(request: Request):
    # Get the request body
    body = await request.json()

    # Access the data
    departure_flight = body.get("departure_flight", [])

    booking_id = len(airline_controller.get_booking_list())+1

    for flight in departure_flight:
        flight_no = flight.get("flight_no")
        departure_date = flight.get("departure_date")

        passengers = flight.get("passenger", [])

        for passenger_group in passengers:
            for passenger_id, passenger_data in passenger_group.items():
                for passenger in passenger_data:
                    title = passenger.get("title")
                    first_name = passenger.get("first_name")
                    last_name = passenger.get("last_name")
                    date_of_birth = passenger.get("date_of_birth")
                    gender = passenger.get("gender")
                    phone_number = passenger.get("phone_number")
                    email = passenger.get("email")
                    extra_service = passenger.get("extra_service", [])

                    for service in extra_service:
                        seat_number = service.get("seat_number")
                        extra_meal = service.get("extra_meal")
                        extra_baggage = service.get("extra_baggage")

                    if seat_number != None:
                        price = 200
                    
                    passenger_obj = Passenger.Passenger(
                        passenger_id, booking_id, title, first_name, last_name, date_of_birth, gender, phone_number, email)
                    
                    airplane = airline_controller.search_airplane_in_flight(flight_no)
                    
                    flight_seat_obj = FlightSeat.FlightSeat(
                        airplane.airplane_id, seat_number, passenger_obj, extra_baggage, extra_meal, price, True)

                    flight_obj = airline_controller.search_flight_from_no(flight_no)
                    
                    flight_obj.add_flight_seat(departure_date,flight_seat_obj)
                    # return departure_date , flight_obj.departure_dates
                    
    
    # Booking.Booking()

    # found flight object

    # for passenger_info in passenger_list:
    #     return seat_number

    # return {"message": flight_seat_obj}


def calculate_duration(departure_time, arrival_time):
    departure = datetime.strptime(departure_time, '%H:%M')
    arrival = datetime.strptime(arrival_time, '%H:%M')
    duration = arrival - departure
    return str(duration)


def create_flight_instance_json():
    with open('./src/database/flight.json', 'r') as f:
        flight_json = json.load(f)

    flight_all = []

    for flight_list in flight_json.values():
        for flight in flight_list:
            flight_data = {
                "flight_no": flight['flight_no'],
                "departure_airport": flight['departure_airport'],
                "destination_airport": flight['destination_airport'],
                "departure_time": flight["departure_time"],
                "arrival_time": flight["arrival_time"],
                "duration_time": calculate_duration(flight["departure_time"], flight["arrival_time"]),
                "airplane": random.randint(1, 50),
                "price": random.randint(1000, 1800),
                "departure_date": []
            }

            for i in range(11):
                departure_date = (
                    datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
                flight_data["departure_date"].append(
                    {departure_date: {"flight_seat": []}})

            flight_all.append(flight_data)

    flight_data = json.dumps(flight_all, indent=4)
    with open('./src/database/flight_instance.json', 'w') as f:
        f.write(flight_data)


def create_instance():
    create_flight_instance_json()

    with open('./src/database/flight_instance.json', "r") as f:
        flight_instances_json = json.load(f)

    with open('./src/database/airplane.json', "r") as f:
        airplane_json = json.load(f)

    # create airport
    with open('./src/database/airport.json', "r") as f:
        airport_json = json.load(f)

    with open('./src/database/user.json', "r") as f:
        user_json = json.load(f)

    user_list = []
    airport_list = []
    airplane_list = []

    for user in user_json:
        user_obj = User.User(user['user_id'], user['username'], user['password'],
                             user['first_name'], user['last_name'], user['phone_number'], user['email'],)
        user_list.append(user_obj)

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

        flight_instance = FlightInstance.FlightInstance(flight_instance_list['flight_no'], departure_airport, destination_airport, flight_instance_list['departure_time'],
                                                        flight_instance_list['arrival_time'], flight_instance_list['duration_time'], airplane_id, flight_instance_list['price'], flight_instance_list['departure_date'])

        flight_instances_obj.append(flight_instance)

    airline_controller.set_flight_instance(flight_instances_obj)

    airline_controller.set_user_list(user_list)


create_instance()
