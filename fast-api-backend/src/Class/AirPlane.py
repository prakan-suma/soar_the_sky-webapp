class AirPlane:
    def __init__(self, airplane_id, model, capacity, seat):
        self.__airplane_id = airplane_id
        self.__model = model
        self.__capacity = capacity
        self.__seat = seat

    @property
    def airplane_id(self):
        return self.__airplane_id

    @property
    def model(self):
        return self.__model

    @property
    def capacity(self):
        return self.__capacity

    @property
    def seat(self):
        return self.__seat

    def to_dict(self):
        return {
            'airplane_id': str(self.__airplane_id),
            'model': self.__model,
            'capacity': self.__capacity,
            'seat': self.__seat
        }
