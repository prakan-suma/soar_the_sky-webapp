
class AirPort:
    def __init__(self, airport_id, airport_code, gate, name, location):
        self.__airport_id = airport_id
        self.__airport_code = airport_code
        self.__gate = gate
        self.__name = name
        self.__location = location

    @property
    def airport_id(self):
        return self.__airport_id

    @property
    def airport_code(self):
        return self.__airport_code

    @property
    def gate(self):
        return self.__gate

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    def to_dict(self):
        return {
            'airport_id': self.__airport_id,
            'airport_code': self.__airport_code,
            'gate': self.__gate,
            'name': self.__name,
            'location': self.__location
        }
