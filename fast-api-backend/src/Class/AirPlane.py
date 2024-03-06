import random
class AirPlane:

    def __init__(self, airplane_id,model,capacity,seat):
        self.__airplane_id  = airplane_id
        self.__model = model
        self.__capacity =  capacity
        self.__seat = seat
        
    def get_airplane_id(self):
        return self.__airplane_id
    
    def create_instance():
        airplane = [
            AirPlane("SA-3499-C","Airbus",500,600),
            AirPlane("S3-0320-C","Airbus",300,300),
            AirPlane("BA-EP33-C","Boeing",500,600),
            AirPlane("UK-PS99-C","Airbus",500,600),
            AirPlane("PW-7893-C","Boeing",300,300),
        ]

        return airplane
    
    def to_dict(self):
        return {
            "airplane_id": self.__airplane_id,
            "model": self.__model,
            "capacity": self.__capacity,
            "seat": self.__seat
        }
    
    
