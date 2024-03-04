# uvicorn main:app --reload
from fastapi import FastAPI
from routers import flights as flights
from src.Controller import AirLineController
from src.Class import AirPlane,AirPort,Flight

app = FastAPI()

@app.get("/")
async def root():
    return "back-end"


@app.get('/api/airplane_all')
async def airplane_all():
    list = []
    for airplanes in  airline_controller.get_airplane_list():
        air = airplanes.to_dict()
        list.append(air)
    return list

@app.get('/api/airport_all/')
async def airport_all():
    air_list = airline_controller.get_airport_list()
    airs = [a.to_dict() for a in air_list ]
    
@app.get('/api/flight')
async def flight():
    return flight_list
    

# flight routes 
app.include_router(flights.router)

# ***-create instance all class-*** 
airline_controller =  AirLineController.AirLineController()  

# create airplane instance 
airplane_list = AirPlane.AirPlane.create_instance()
airline_controller.set_airplane_list(airplane_list)

#create airport instance
airport_list = AirPort.AirPort.create_instance()
airline_controller.set_airport_list(airport_list)

# create departure flights isinstance
departure_flight_list = [
    Flight.Flight("SA88234","60",airline_controller.search_from_id(1),airline_controller.search_from_id(2)),
    Flight.Flight("FKN2340","90",airline_controller.search_from_id(1),airline_controller.search_from_id(3)),
    Flight.Flight("IEO6442","120",airline_controller.search_from_id(1),airline_controller.search_from_id(4)),
    Flight.Flight("JAZZ204","50",airline_controller.search_from_id(1),airline_controller.search_from_id(5)),
]
# create destination flights isinstance
departure_flight_list = [
    Flight.Flight("3EFK424","60",airline_controller.search_from_id(2),airline_controller.search_from_id(1)),
    Flight.Flight("KKL20E4","90",airline_controller.search_from_id(3),airline_controller.search_from_id(1)),
    Flight.Flight("HJS8990","120",airline_controller.search_from_id(4),airline_controller.search_from_id(1)),
    Flight.Flight("ROV9302","50",airline_controller.search_from_id(5),airline_controller.search_from_id(1)),
]


