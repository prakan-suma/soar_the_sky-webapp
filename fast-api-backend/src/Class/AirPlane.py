import random
class AirPlane:

    def __init__(self, airplane_id,model,capacity,seat):
        self.__airplane_id  = airplane_id
        self.__model = model
        self.__capacity =  capacity
        self.__seat = seat
    
    def create_instance():
        airplane = []
        
        for _ in range(100):
            airplane_id = f"SA-{random.randint(1000,9999)}-"
            model = f"{random.choice(["Boeing" , 'Airbus'])}-{random.randint(700,900)}"
            capacity = random.randint(50,500)
            seat = random.choice([300,600])
            airplane.append(AirPlane(airplane_id,model,capacity,seat))
        
        return airplane 
    
    def to_dict(self):
        return {
            "airplane_id": self.__airplane_id,
            "model": self.__model,
            "capacity": self.__capacity,
            "seat": self.__seat
        }
    
    
