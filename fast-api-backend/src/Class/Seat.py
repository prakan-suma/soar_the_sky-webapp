class Seat:
    def __init__(self, airplane_id,seat_number):
        self.__airplane_id = airplane_id
        self.__seat_number = seat_number
        
    @property
    def airplane_id(self):
        return self.__airplane_id
    
    @property
    def seat_number(self):
        return self.__seat_number
    