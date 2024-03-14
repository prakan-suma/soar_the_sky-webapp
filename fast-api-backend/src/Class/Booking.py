import json

class Booking:
    def __init__(self, booking_id, flight, booking_date,  payment, ticket_list=None):
        self.__booking_id = booking_id
        self.__flight = flight
        self.__booking_date = booking_date
        self.__status = False
        self.__ticket_list = ticket_list if ticket_list is not None else []
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
    
    def set_ticket(self,ticket):
        self.__ticket_list.append(ticket)
        
    def add_booking_to_json(self, filename="./src/database/booking.json"):
        try:
            with open(filename, "r+") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Error: Invalid JSON format in {filename}. Creating a new file.")
                    data = []
        except FileNotFoundError:
            # File doesn't exist, create an empty list
            data = []

        data.append(self.to_dict())

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def set_status(self, new_status):
        if not isinstance(new_status, bool):
            raise ValueError("Status must be a boolean value (True or False).")
        self.__status = new_status

    def to_dict(self):
        return {
            # Already addressed in previous responses
            "booking_id": str(self.booking_id),
            "flight": self.flight.to_dict(),
            # Convert date to string
            "booking_date": self.booking_date.strftime("%Y-%m-%d"),
            "status": self.status,
            "ticket_list": [ticket.to_dict() for ticket in self.ticket_list],
            "payment": self.payment.to_dict() if self.payment else None, }
