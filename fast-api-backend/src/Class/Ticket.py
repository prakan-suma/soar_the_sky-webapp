class Ticket:
    def __init__(self, ticket_id, flight_id, gate, passenger, baggage):
        self.__ticket_id = ticket_id
        self.__flight_id = flight_id
        self.__gate = gate
        self.__passenger = passenger
        self.__baggage = baggage

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def flight_id(self):
        return self.__flight_id

    @property
    def gate(self):
        return self.__gate

    @property
    def passenger(self):
        return self.__passenger

    @property
    def baggage(self):
        return self.__baggage
