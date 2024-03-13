import json

import datetime


class AirLineController:

    def __init__(self):
        self.__flight_instance_list = []
        self.__airplane_list = []
        self.__airport_list = []
        self.__user_list = []
        self.__booking_list = []
        

    # getter
    def get_airplane_list(self):
        return self.__airplane_list

    def get_airport_list(self):
        return self.__airport_list

    def get_flight_list(self):
        return self.__flight_instance_list

    def get_user_list(self):
        return self.__user_list
    
    def get_booking_list(self):
        return self.__booking_list
    
    # setter

    def set_user_list(self,user_list):
        self.__user_list = user_list

    def set_airport_list(self, airport_list):
        self.__airport_list = airport_list

    def set_airplane_list(self, airplane_list):
        self.__airplane_list = airplane_list

    def set_flight_instance(self, flight_list):
        self.__flight_instance_list = flight_list
        
    def add_booking(self,booking):
        self.get_booking_list().append(booking)
        
    # search method
    
    def search_booking_from_id(self,booking_id):
        for booking in self.__booking_list:
            if booking_id == booking.booking_id:
                return booking
        
    def search_flight_from_no(self,flight_no):
        for flight in self.__flight_instance_list:
            if flight_no == flight.flight_no:
                return flight
            
    def search_airplane_in_flight(self,flight_no):
        for flight in self.__flight_instance_list:
            if flight_no == flight.flight_no:
                return flight.airplane
    
    def search_flight_one_way(self, departureAirport, destinationAirport, departureDate):
        flight_found = []
    # search flight from departureAirport,destinationAirport,departureDate
        for flight in self.__flight_instance_list:
            if flight.departure_airport.airport_code == departureAirport and flight.destination_airport.airport_code == destinationAirport:
                flight_found.append(flight)

        return flight_found


    def search_flight_round_trip(self, departureAirport, destinationAirport, departureDate, returnDate):
        departure_flight = []
        return_flight = []

        # search flight from departureAirport,destinationAirport,departureDate,destinationDate
        for flight in self.__flight_instance_list:
            # found departure flights
            if flight.departure_airport.airport_code == departureAirport and flight.destination_airport.airport_code == destinationAirport:
                departure_flight.append(flight)
                
            if flight.departure_airport.airport_code == destinationAirport and flight.destination_airport.airport_code == departureAirport :
                return_flight.append(flight)

        return departure_flight, return_flight

    def search_airport_from_id(self, airport_id):
        for a in self.__airport_list:
            if airport_id == a.get_airport_id():
                airport_obj = a
            else:
                None

        return airport_obj

    def search_airplane_from_id(self, airplane_id):
        for a in self.__airplane_list:
            if airplane_id == a.get_airplane_id():
                airplane_obj = a
            else:
                None

        return airplane_obj
