import json 
from src.Class import AirPlane,AirPort,Flight,FlightSeat,FlightInstance   

import datetime

class AirLineController:
    
    def __init__(self):
        self.__flight_instance_list = []
        self.__airplane_list = []
        self.__airport_list = []
    
    # getter 
    def get_airplane_list(self):
        return self.__airplane_list
    
    def get_airport_list(self):
        return self.__airport_list
    
    def search_from_id(self,airport_id):
        for a in self.__airport_list:
            if airport_id == a.get_airport_id():
                airport_obj = a
            else:
                None
                
        return airport_obj
    
    def set_airport_list(self,airport_list):
        self.__airport_list = airport_list
    # setter 
    def set_airplane_list(self,airplane_list):
        self.__airplane_list = airplane_list         
        