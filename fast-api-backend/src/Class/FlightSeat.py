from src.Class.Seat import Seat 

class FlightSeat(Seat):
    def __init__(self, passenger, airplane_seat, baggage_weight=False, extra_meal=False, price=None, status=False):
        self.__passenger = passenger
        self.__airplane_seat = airplane_seat
        self.__baggage_weight = baggage_weight
        self.__extra_meal = extra_meal
        self.__price = price
        self.__status = status