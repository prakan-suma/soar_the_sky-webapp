from src.Class.Flight import Flight


class FlightInstance(Flight):
    def __init__(self, flight_no, departure_airport, destination_airport, departure_time,arrival_time, duration_time, airplane, price ,departure_date):
        super().__init__(flight_no, departure_airport, destination_airport, departure_time,arrival_time)
        self.__duration_time = duration_time
        self.__airplane = airplane
        self.__price = price     
        self.__departure_dates = departure_date

    @property
    def duration_time(self):
        return self.__duration_time

    @property
    def airplane(self):
        return self.__airplane

    @property
    def price(self):
        return self.__price

    @property
    def departure_dates(self):
        return self.__departure_dates

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "duration_time": self.__duration_time,
            "airplane": self.__airplane.to_dict(),
            "price": self.__price,
            "departure_dates": self.__departure_dates
        })
        return base_dict
