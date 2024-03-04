import json 
from src.Class import AirPlane,AirPort,Flight,FlightSeat,FlightInstance   

import datetime

class AirLineController:
    
    # def __init__(self, flight_instance,):
    #     self.__flight_instance_list = flight_instance
    
    
    def search_one_way(self,departure_airport,destination_airport,departure_date):
        
        with open('./src/database/flights.json') as f:
            flight_json = json.load(f)
            
        with open('./src/database/flights_instance.json') as f:
            flight_instance_json = json.load(f)
        
        with open('./src/database/airport.json') as f:
            airport_json = json.load(f)
        
        with open('./src/database/airplane.json') as f:
            airplane_json = json.load(f)
        
        found_flights = []
        for flight_instance_list in flight_instance_json:
            flight_instance_date = flight_instance_list['departure_date'].split('T')[0]
            
            if flight_instance_date == departure_date:
                for flight_list in flight_json:
                    if flight_instance_list['flight_no'] == flight_list['flight_no']:
                        flight_no = flight_list['flight_no']
                        duration_time = flight_list['duration_time']
                        
                        for airport_list in airport_json:
                            if airport_list['airport_id'] == flight_list['departure_airport']:
                                departure_airport_obj = AirPort.AirPort(airport_list['airport_id'],airport_list['airport_code'],airport_list['gate'],airport_list['name'],airport_list['location'])
                                
                            if airport_list['airport_id'] == flight_list['destination_airport']:
                                destination_airport_obj = AirPort.AirPort(airport_list['airport_id'],airport_list['airport_code'],airport_list['gate'],airport_list['name'],airport_list['location'])
                
                for airplane_list in airplane_json:
                    if airplane_list['airplane_id'] == flight_instance_list['airplane_id']:
                        airplane_obj = AirPlane.AirPlane(airplane_list['airplane_id']  ,airplane_list['air_type']  ,airplane_list['model']  ,airplane_list['capacity']  ,airplane_list['seat']  )

                
                flight_instance_object = FlightInstance.FlightInstance(airplane=airplane_obj,flight_seat=None,departure_date=flight_instance_list['departure_date'],destination_date=flight_instance_list['destination_date'],departure_time=flight_instance_list['departure_time'],arrival_time=flight_instance_list['arrival_time'],price=flight_instance_list['price'],flight_no=flight_no,duration_time=duration_time,departure_airport=departure_airport_obj,destination_airport=destination_airport_obj)
                
                flight_instance_dict = flight_instance_object.to_dict()
                
                if flight_instance_object.get_departure_airport().get_airport_code()  == departure_airport and flight_instance_object.get_destination_airport().get_airport_code()  == destination_airport:  
                    found_flights.append(flight_instance_dict)

            
        return found_flights