class PaymentMethod:
    def __init__(self, method_id, method_type, method_provider, method_details):
        self.__method_id = method_id
        self.__method_type = method_type
        self.__method_provider = method_provider
        self.__method_details = method_details

    # Getter methods
    def get_method_id(self):
        return self.__method_id

    def get_method_type(self):
        return self.__method_type

    def get_method_provider(self):
        return self.__method_provider

    def get_method_details(self):
        return self.__method_details
