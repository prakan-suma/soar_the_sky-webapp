from src.Class.Seat import Seat


class FlightSeat(Seat):
    def __init__(self, airplane_id, seat_number, passenger, baggage_weight=False, extra_meal=False, price=0, status=False):
        super().__init__(airplane_id, seat_number)
        self._passenger = passenger
        self._baggage_weight = baggage_weight
        self._extra_meal = extra_meal
        self._price = price
        self._status = status

    @property
    def passenger(self):
        return self._passenger

    @property
    def baggage_weight(self):
        return self._baggage_weight

    @property
    def extra_meal(self):
        return self._extra_meal

    @property
    def price(self):
        return self._price

    @property
    def status(self):
        return self._status

    def to_dict(self):
        return {
            "airplane_id": self.airplane_id,
            "seat_number": self.seat_number,
            "passenger": self.passenger.to_dict() ,
            "baggage_weight": self.baggage_weight,
            "extra_meal": self.extra_meal,
            "price": self.price,
            "status": self.status,
        }
