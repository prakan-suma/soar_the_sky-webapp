class AirPort:
    def __init__(self, airport_id, airport_code, gate, name, location):
        self.__airport_id = airport_id
        self.__airport_code = airport_code
        self.__gate =  gate
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

    def create_instance():
        thailand_airports = [
            AirPort(1, "BKK", ["Gate A", "Gate B", "Gate C"],
                    "Suvarnabhumi Airport", "Bangkok"),
            AirPort(2, "DMK", ["Gate A", "Gate B", "Gate C"],
                    "Don Mueang International Airport", "Bangkok"),
            AirPort(3, "CNX", ["Gate F", "Gate G"],
                    "Chiang Mai International Airport", "Chiang Mai"),
            AirPort(4, "HKT", ["Gate H", "Gate I"],
                    "Phuket International Airport", "Phuket"),
            AirPort(5, "USM", ["Gate J", "Gate K"],
                    "Samui Airport", "Koh Samui"),
            AirPort(6, "CEI", ["Gate L"],
                    "Chiang Rai International Airport", "Chiang Rai"),
            AirPort(7, "URT", ["Gate M"],
                    "Surat Thani Airport", "Surat Thani"),
            AirPort(8, "KBV", ["Gate N"],
                    "Krabi International Airport", "Krabi"),
            AirPort(9, "HDY", ["Gate O"],
                    "Hat Yai International Airport", "Hat Yai"),
            AirPort(10, "UTP", [
                    "Gate P"], "U-Tapao Rayong-Pattaya International Airport", "Rayong/Pattaya"),
            AirPort(11, "TDX", ["Gate Q"], "Trat Airport", "Trat"),
            AirPort(12, "UTH", ["Gate R"],
                    "Udon Thani International Airport", "Udon Thani"),
            AirPort(
                13, "NST", ["Gate S"], "Nakhon Si Thammarat Airport", "Nakhon Si Thammarat"),
            AirPort(14, "LPT", ["Gate T"], "Lampang Airport", "Lampang"),
            AirPort(15, "THS", ["Gate U"], "Sukhothai Airport", "Sukhothai"),
        ]

        return thailand_airports
    
    def to_dict(self):
        airport_dict = {
            "airport_id": self.__airport_id,
            "airport_code": self.__airport_code,
            "gate": self.__gate,
            "name": self.__name,
            "location": self.__location
        }
        return airport_dict
