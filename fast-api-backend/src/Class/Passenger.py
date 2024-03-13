class Passenger:
    def __init__(self, passenger_id, booking_id,title,first_name,last_name, date_of_birth, gender, phone_number=None, email=None):
        self._passenger_id = passenger_id
        self._booking_id = booking_id
        self._title = title
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._phone_number = phone_number
        self._email = email

    @property
    def passenger_id(self):
        return self._passenger_id

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def title(self):
        return self._title
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def gender(self):
        return self._gender

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def email(self):
        return self._email
    
    def to_dict(self):
        return {
            "passenger_id": self.passenger_id,
            "booking_id": self.booking_id,
            "title": self.title,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "email": self.email,
        }

