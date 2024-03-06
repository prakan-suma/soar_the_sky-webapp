import json

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

    def get_flight_list(self):
        return self.__flight_instance_list
    # setter

    def set_airport_list(self, airport_list):
        self.__airport_list = airport_list

    def set_airplane_list(self, airplane_list):
        self.__airplane_list = airplane_list

    def set_flight_instance(self, flight_list):
        self.__flight_instance_list = flight_list

    # search method
    def search_flight_one_way(self, departureAirport, destinationAirport, departureDate):

        flight_found = []

        # search flight from departureAirport,destinationAirport,departureDate
        for flight in self.__flight_instance_list:
            if flight.get_departure_airport().get_airport_code() == departureAirport and flight.get_destination_airport().get_airport_code() == destinationAirport and flight.get_departure_date() == departureDate:
                flight_found.append(flight)

        return flight_found

    def search_flight_round_trip(self, departureAirport, destinationAirport, departureDate, returnDate):
        departure_flight = []
        return_flight = []

        # search flight from departureAirport,destinationAirport,departureDate,destinationDate
        for flight in self.__flight_instance_list:
            # found departure flights
            if flight.get_departure_airport().get_airport_code() == departureAirport and flight.get_destination_airport().get_airport_code() == destinationAirport and flight.get_departure_date() == departureDate:
                departure_flight.append(flight)

            # found return flight
            if flight.get_departure_airport().get_airport_code() == destinationAirport and flight.get_destination_airport().get_airport_code() == departureAirport and flight.get_departure_date() == returnDate:
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
