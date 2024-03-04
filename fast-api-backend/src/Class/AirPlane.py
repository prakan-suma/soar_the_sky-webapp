class AirPlane:

    def __init__(self, airplane_id,air_type,model,capacity,seat):
        self.__airplane_id  = airplane_id
        self.__air_type = air_type
        self.__model = model
        self.__capacity =  capacity
        self.__seat = seat
    
    def to_dict(self):
        return {
            "airplane_id": self.__airplane_id,
            "air_type": self.__air_type,
            "model": self.__model,
            "capacity": self.__capacity,
            "seat": self.__seat
        }
    
    
