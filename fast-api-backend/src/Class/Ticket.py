class Ticket:
    def __init__(self, ticket_id, flight_no, passenger_name, class_type, departure_date, flight_seat,departure_airport, destination_airport, boarding_time, baggage, gate, barcode_id):
        self.__ticket_id = ticket_id
        self.__flight_no = flight_no
        self.__passenger_name = passenger_name
        self.__class_type = class_type
        self.__departure_date = departure_date
        self.__flight_seat = flight_seat
        self.__departure_airport = departure_airport
        self.__destination_airport = destination_airport
        self.__boarding_time = boarding_time
        self.__baggage = baggage
        self.__gate = gate
        self.__barcode_id = barcode_id

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def flight_no(self):
        return self.__flight_no

    @property
    def passenger_name(self):
        return self.__passenger_name

    @property
    def class_type(self):
        return self.__class_type

    @property
    def departure_date(self):
        return self.__departure_date

    @property
    def flight_seat(self):
        return self.__flight_seat

    @property
    def departure_airport(self):
        return self.__departure_airport

    @property
    def destination_airport(self):
        return self.__destination_airport

    @property
    def boarding_time(self):
        return self.__boarding_time

    @property
    def baggage(self):
        return self.__baggage

    @property
    def gate(self):
        return self.__gate

    @property
    def barcode_id(self):
        return self.__barcode_id

    def to_dict(self):

        return {
            "ticket_id": self.ticket_id,
            "flight_no": self.flight_no,
            "passenger_name": self.passenger_name,
            "class_type": self.class_type,
            "departure_date": self.departure_date,
            "flight_seat": self.flight_seat,
            "departure_airport": self.departure_airport,
            "destination_airport": self.destination_airport,
            "boarding_time": self.boarding_time,
            "baggage": self.baggage,
            "gate": self.gate,
            "barcode_id": self.barcode_id,
        }
