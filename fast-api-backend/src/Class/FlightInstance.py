from src.Class.Flight import Flight


class FlightInstance(Flight):
    def __init__(self, flight_no, duration_time, departure_airport, destination_airport, airplane, flight_seat, departure_date, destination_date, departure_time, arrival_time, price):
        super().__init__(flight_no, duration_time, departure_airport, destination_airport)
        self.__airplane = airplane
        self.__flight_seat = flight_seat
        self.__departure_date = departure_date
        self.__destination_date = destination_date
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__price = price

    # Getter methods
    def get_airplane(self):
        return self.__airplane

    def get_flight_seat(self):
        return self.__flight_seat

    def get_departure_date(self):
        return self.__departure_date

    def get_destination_date(self):
        return self.__destination_date

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_price(self):
        return self.__price

    def get_departure_airport(self):
        return self._Flight__departure_airport

    def get_destination_airport(self):
        return self._Flight__destination_airport