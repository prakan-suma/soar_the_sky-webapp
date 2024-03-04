class AirPort:
    def __init__(self, airport_id, airport_code, gate, name, location):
        self.__airport_id = airport_id
        self.__airport_code = airport_code
        self.__gate = gate
        self.__name = name
        self.__location = location

    def get_airport_id(self):
        return self.__airport_id

    def get_airport_code(self):
        return self.__airport_code

    def get_gate(self):
        return self.__gate

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def to_dict(self):
        airport_dict = {
            "airport_id": self.__airport_id,
            "airport_code": self.__airport_code,
            "gate": self.__gate,
            "name": self.__name,
            "location": self.__location
        }
        return airport_dict
