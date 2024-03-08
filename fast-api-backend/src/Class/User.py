class User:
    def __init__(self, user_id, username, password, first_name, last_name, phone_number, email, booking_list):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email
        self.__booking_list = booking_list
    
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def email(self):
        return self.__email
    
    @property
    def booking_list(self):
        return self.__booking_list
