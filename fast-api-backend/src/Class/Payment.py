class Payment:
    def __init__(self, payment_id, amount, payment_date, payment_method):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_date = payment_date
        self.__payment_method = payment_method

    def get_payment_id(self):
        return self.__payment_id

    def get_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date

    def get_payment_method(self):
        return self.__payment_method
