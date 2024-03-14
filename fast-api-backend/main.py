import json
import random
import uuid
from fastapi import FastAPI, Body, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from src.Controller import AirLineController
from src.Class import AirPlane, AirPort, FlightInstance, User, Passenger, Booking, Payment, PaymentMethod, FlightSeat, Ticket
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


@app.post('/api/booking/payment/')
async def booking_payment(request: Request):
    body = await request.json()
    booking_id = body.get('booking_id')
    payment_id = body.get('payment_id')
    referral_code = body.get('referral_code')
    status = body.get('status')

    # search booking id in airline
    booking = airline_controller.search_booking_from_id(booking_id)

    # if payment_id != booking.payment.payment_id and referral_code != booking.payment.payment_method.referral_code and status != True:
    # return {"message" : "Unsuccessful transaction" }

    # set status
    booking.set_status(True)
    booking.payment.payment_method.set_status(True)

    ticket_list = []
    # create ticket
    for departure_date_dict in booking.flight.departure_dates:
        for date, seats in departure_date_dict.items():
            if seats:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                departure_time = datetime.strptime(
                    booking.flight.departure_time, "%H:%M")
                boarding_time = departure_time - timedelta(hours=1)
                for seat in seats:
                    passenger = seat.passenger
                    ticket_id = str(uuid.uuid4())
                    flight_no = booking.flight.flight_no
                    passenger_name = f"{passenger.title}. {
                        passenger.first_name} {passenger.last_name}"
                    class_type = "Economy"
                    departure_date = date
                    flight_seat = seat.seat_number
                    departure_airport = booking.flight.departure_airport.airport_code
                    destination_airport = booking.flight.destination_airport.airport_code
                    boarding_time_str = boarding_time.strftime("%H:%M")
                    baggage = "SA Extra" if seat.baggage_type else "SA Lite"
                    gate = booking.flight.gate
                    barcode_id = f"SA0{uuid.uuid4()}"

                    ticket = Ticket.Ticket(ticket_id, flight_no, passenger_name, class_type, departure_date, flight_seat,
                                           departure_airport, destination_airport, boarding_time_str, baggage, gate, barcode_id)

                    ticket_list.append(ticket.to_dict())
                    booking.set_ticket(ticket)

    # Add booking object to json
    booking.add_booking_to_json()

    return [{"message": "Successful transaction"}, {"tickets": ticket_list }]
@app.post("/api/one-way/booking/")
async def one_way_booking(request: Request):
    # Get the request body
    body = await request.json()

    # Access the data
    booking_id = len(airline_controller.get_booking_list()) + 1
    departure_flight = body.get("departure_flight", [])
    return_flight = body.get("return_flight", [])
    total_seat_price = 0
    passenger_amount = 0

    flight_objs = process_flight(departure_flight, return_flight, booking_id, total_seat_price, passenger_amount)

    # create Payment
    payment_id = uuid.uuid4()
    price_sum = sum(flight.price * passenger_amount + total_seat_price for flight in flight_objs)
    today = date.today()
    payment_method = PaymentMethod.PaymentMethod(payment_id, price_sum, uuid.uuid4())
    payment = Payment.Payment(payment_id, price_sum, today, payment_method)
    booking = Booking.Booking(booking_id, flight_objs, today, payment)

    # add booking into airline
    airline_controller.add_booking(booking)

    # return booking.to_dict()
    return booking


@app.post("/api/round-trip/booking/")
async def round_trip_booking(request: Request):
    body = await request.json()

    booking_id = len(airline_controller.get_booking_list()) + 1
    total_seat_price = 0
    passenger_amount = 0

    # Process departure flight
    departure_flight = body.get("departure_flight", [])
    departure_flight_obj = process_flight(
        departure_flight, booking_id, total_seat_price, passenger_amount)

    # Process return flight
    return_flight = body.get("return_flight", [])
    return_flight_obj = process_flight(
        return_flight, booking_id, total_seat_price, passenger_amount)

    return passenger_amount
    # Create Payment
    payment_id = uuid.uuid4()
    price_sum = (departure_flight_obj.price * passenger_amount) + \
        (return_flight_obj.price * passenger_amount) + total_seat_price
    today = date.today()
    payment_method = PaymentMethod.PaymentMethod(
        payment_id, price_sum, uuid.uuid4())
    payment = Payment.Payment(payment_id, price_sum, today, payment_method)

    # Create Booking
    booking_departure = Booking.Booking(booking_id, departure_flight_obj, today, payment)
    booking_return = Booking.Booking(booking_id, return_flight_obj, today, payment)

    # Add booking to airline
    airline_controller.add_booking(booking_departure)
    airline_controller.add_booking(booking_return)

    return booking_departure,booking_return
def process_flight(departure_flight, return_flight, booking_id, total_seat_price, passenger_amount):
    flight_objs = []
    for flights in [departure_flight, return_flight]:
        for flight in flights:
            flight_no = flight.get("flight_no")
            departure_date = flight.get("departure_date")
            passengers = flight.get("passenger", [])

            for passenger_group in passengers:
                passenger_amount += len(passenger_group)
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

                            if seat_number is not None:
                                price = 200
                                total_seat_price += price

                        airplane = airline_controller.search_airplane_in_flight(flight_no)
                        flight_obj = airline_controller.search_flight_from_no(flight_no)

                        passenger_obj = Passenger.Passenger(
                            passenger_id, booking_id, title, first_name, last_name, date_of_birth, gender, phone_number, email)

                        flight_seat_obj = FlightSeat.FlightSeat(
                            airplane.airplane_id, seat_number, passenger_obj, extra_baggage, extra_meal, price, True)

                        # add flight seat and passenger in to departure_date
                        flight_obj.add_flight_seat(departure_date, flight_seat_obj)
                        flight_objs.append(flight_obj)

    return flight_objs


def calculate_duration(departure_time, arrival_time):
    departure = datetime.strptime(departure_time, '%H:%M')
    arrival = datetime.strptime(arrival_time, '%H:%M')
    duration = arrival - departure
    return str(duration)


def create_flight_instance_json():
    with open('./src/database/flight.json', 'r') as f:
        flight_json = json.load(f)

    flight_all = []
    airplane = random.choice(airline_controller.get_airplane_list())

    for flight_list in flight_json.values():
        for flight in flight_list:
            flight_data = {
                "flight_no": flight['flight_no'],
                "departure_airport": flight['departure_airport'],
                "destination_airport": flight['destination_airport'],
                "departure_time": flight["departure_time"],
                "arrival_time": flight["arrival_time"],
                "duration_time": calculate_duration(flight["departure_time"], flight["arrival_time"]),
                "gate": None,
                "airplane": airplane.airplane_id,
                "price": random.randint(1000, 1800),
                "departure_date": []
            }

            airport = airline_controller.search_airport_from_id(
                flight['departure_airport'])
            gate = random.choice(airport.gate)
            flight_data['gate'] = gate

            for i in range(11):
                departure_date = (
                    datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
                flight_data["departure_date"].append(
                    {departure_date: []})

            flight_all.append(flight_data)

    flight_data = json.dumps(flight_all, indent=4)
    with open('./src/database/flight_instance.json', 'w') as f:
        f.write(flight_data)


def create_instance():
    # with open('./src/')

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

    create_flight_instance_json()

    with open('./src/database/flight_instance.json', "r") as f:
        flight_instances_json = json.load(f)

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

        flight_instance = FlightInstance.FlightInstance(flight_instance_list['flight_no'], departure_airport, destination_airport, flight_instance_list['departure_time'], flight_instance_list[
                                                        'arrival_time'], flight_instance_list['duration_time'], flight_instance_list['gate'], airplane_id, flight_instance_list['price'], flight_instance_list['departure_date'])

        flight_instances_obj.append(flight_instance)

    airline_controller.set_flight_instance(flight_instances_obj)

    airline_controller.set_user_list(user_list)


create_instance()
