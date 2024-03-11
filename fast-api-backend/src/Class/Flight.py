
class Flight:
    def __init__(self, flight_no, departure_airport, destination_airport, departure_time, arrival_time):
        self.__flight_no = flight_no
        self.__departure_airport = departure_airport
        self.__destination_airport = destination_airport
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time

    @property
    def flight_no(self):
        return self.__flight_no

    @property
    def departure_airport(self):
        return self.__departure_airport

    @property
    def destination_airport(self):
        return self.__destination_airport

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def arrival_time(self):
        return self.__arrival_time

    def to_dict(self):
        return {
            'flight_no': self.__flight_no,
            'departure_airport': self.__departure_airport.to_dict(),
            'destination_airport': self.__destination_airport.to_dict(),
            'departure_time': self.__departure_time,
            'arrival_time': self.__arrival_time
        }