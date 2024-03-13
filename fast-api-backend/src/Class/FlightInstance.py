from src.Class.Flight import Flight
import json

class FlightInstance(Flight):
    def __init__(self, flight_no, departure_airport, destination_airport, departure_time,arrival_time, duration_time, airplane, price ,departure_date):
        super().__init__(flight_no, departure_airport, destination_airport, departure_time,arrival_time)
        self.__duration_time = duration_time
        self.__airplane = airplane
        self.__price = price     
        self.__departure_dates = departure_date

    @property
    def duration_time(self):
        return self.__duration_time

    @property
    def airplane(self):
        return self.__airplane

    @property
    def price(self):
        return self.__price

    @property
    def departure_dates(self):
        return self.__departure_dates

    def add_flight_seat(self, departure_date, flight_seat_obj):
        with open('./src/database/flight_instance.json', 'r+') as flight_data_file:
            flight_data = json.load(flight_data_file)

            # Find the flight with the matching flight number
            for flight_info in flight_data:
                if flight_info.get("flight_no") == self.flight_no:
                    # Access the departure_date list
                    departure_date_list = flight_info.get("departure_date", [])

                    # Find the dictionary with the matching departure_date
                    for date_dict in departure_date_list:
                        date_str = list(date_dict.keys())[0]
                        if date_str == departure_date:
                            # Append the flight_seat_obj to the flight_seat list
                            date_dict[date_str]["flight_seat"].append(flight_seat_obj.__dict__)
                            break

                    # Move the file pointer to the beginning of the file
                    flight_data_file.seek(0)
                    # Write the updated JSON data back to the file
                    json.dump(flight_data, flight_data_file, indent=4)
                    flight_data_file.truncate()
                    break

    # def add_flight_seat(self, departure_date, flight_seat_obj):

    #     # with open('./src/database/flight_instance.json', 'r+') as flight_data_file:
    #     #     flight_data = json.load(flight_data_file)

    #     #     for flight_info in flight_data:
    #     #         flight_no = flight_info["flight_no"]
    #     #         if flight_no == self.flight_no:
    #     #             for date_all in flight_info["departure_date"]:
    #     #                 for date in date_all:
    #     #                     if departure_date == date:
        
    #     with open('./src/database/flight_instance.json', 'r+') as flight_data_file:
    #         flight_data = json.load(flight_data_file)


    #     # Find the flight with the matching flight number
    #     for flight_info in flight_data:
    #         # Check if flight_info is a dictionary (assuming it should be)
    #         if isinstance(flight_info, dict):
    #             flight_no = flight_info.get("flight_no")

    #             # Check if flight number matches and departure_date exists
    #             if flight_no == self.flight_no and flight_info.get("departure_date"):
    #                 departure_date_info = flight_info["departure_date"]

    #                 # Access the specific date information if it exists
    #                 if departure_date in departure_date_info:
    #                     # Append the flight seat object to the existing flight seat list
    #                     departure_date_info[departure_date]["flight_seat"].append(flight_seat_obj.__dict__)
    #                     break  # Stop iterating after finding the matching date
                        

    

    
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            "duration_time": self.__duration_time,
            "airplane": self.__airplane.to_dict(),
            "price": self.__price,
            "departure_dates": self.__departure_dates
        })
        return base_dict
