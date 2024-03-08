class Booking:
    def __init__(self, booking_id, flight, booking_date, status, ticket_list, payment):
        self.__booking_id = booking_id
        self.__flight = flight
        self.__booking_date = booking_date
        self.__status = status
        self.__ticket_list = ticket_list
        self.__payment = payment

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def flight(self):
        return self.__flight

    @property
    def booking_date(self):
        return self.__booking_date

    @property
    def status(self):
        return self.__status

    @property
    def ticket_list(self):
        return self.__ticket_list

    @property
    def payment(self):
        return self.__payment
