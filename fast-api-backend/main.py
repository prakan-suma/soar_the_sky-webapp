# uvicorn main:app --reload
from fastapi import FastAPI
from routers import flights as flights
from src.Controller import AirLineController
from src.Class import AirPlane,AirPort

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
    a = airline_controller.search_from_id(2)
    for al in a:
        al = a.to_dict()    
    return  al 

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

# create flights isinstance


