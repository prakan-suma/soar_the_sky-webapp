class Flight:

    def __init__(self, flight_no, duration_time, departure_airport, destination_airport):
        self.__flight_no = flight_no
        self.__duration_time = duration_time
        self.__departure_airport = departure_airport
        self.__destination_airport = destination_airport

    # Getter methods
    def get_flight_no(self):
        return self.__flight_no

    def get_duration_time(self):
        return self.__duration_time

    def get_departure_airport(self):
        return self.__departure_airport

    def get_destination_airport(self):
        return self.__destination_airport
    
    
    def to_dict(self):
        flight_dict = {
            "flight_no": self.__flight_no,
            "duration_time": self.__duration_time,
            "departure_airport": self.__departure_airport.to_dict(),
            "destination_airport": self.__destination_airport.to_dict()
        }
        return flight_dict