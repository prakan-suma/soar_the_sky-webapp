from src.Class.Flight import Flight
import json


class FlightInstance(Flight):
    def __init__(self, flight_no, departure_airport, destination_airport, departure_time, arrival_time, duration_time, airplane, price, departure_date):
        super().__init__(flight_no, departure_airport,
                         destination_airport, departure_time, arrival_time)
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

    def add_flight_seat(self, departure_date, flight_seat_obj):
        # Find the dictionary that contains the departure_date as a key
        for date_dict in self.__departure_dates:
            if departure_date in date_dict:
                date_dict[departure_date].append(flight_seat_obj)
                break
        else:
            print(f"Departure date {departure_date} not found.")

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "duration_time": self.__duration_time,
            "airplane": self.__airplane.to_dict(),
            "price": self.__price,
            "departure_dates": [{"date": list(date_dict.keys())[0], "flight_seats": [seat.to_dict() for seat in list(date_dict.values())[0]]} for date_dict in self.__departure_dates]
        })
        return base_dict
