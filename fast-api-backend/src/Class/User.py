import json


class User:
    def __init__(self, user_id, username, password, first_name, last_name, phone_number, email):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email
        self.__booking_list = []

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

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
        }

    def add_user_to_json(self, filename="./src/database/user.json"):
        user_data = self.to_dict()
        try:
            with open(filename, 'r+') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []

            users.append(user_data)

            # Write the updated user list back to the JSON file
            with open(filename, 'w') as f:
                # Add indentation for readability
                json.dump(users, f, indent=4)

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error adding user to JSON: {e}")
