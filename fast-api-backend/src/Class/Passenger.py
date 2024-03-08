class Passenger:
    def __init__(self, passenger_id, booking_id, name, age, gender, seat_number):
        self.__passenger_id = passenger_id
        self.__booking_id = booking_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__seat_number = seat_number

    # Getter methods
    def get_passenger_id(self):
        return self.__passenger_id

    def get_booking_id(self):
        return self.__booking_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_seat_number(self):
        return self.__seat_number
