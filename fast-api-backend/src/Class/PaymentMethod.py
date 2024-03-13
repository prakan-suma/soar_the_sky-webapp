class PaymentMethod:
    def __init__(self, payment_id, total_price, referral_code):
        self.__payment_id = payment_id
        self.__bank_name = "SCB"
        self.__bank_account_no = "06543987001"
        self.__total_price = total_price
        self.__referral_code = referral_code
        self.__status = False

    @property
    def payment_id(self):
        return self.__payment_id
    
    @property
    def bank_name(self):
        return self.__bank_name

    @property
    def total_price(self):
        return self.__total_price
    
    @property
    def bank_account_no(self):
        return self.__bank_account_no

    @property
    def referral_code(self):
        return self.__referral_code

    @property
    def status(self):
        return self.__status

    # Optional setter method for status (consider security implications)
    def set_status(self, new_status):
        if not isinstance(new_status, bool):
            raise ValueError("Status must be a boolean value (True or False).")
        self.__status = new_status
        
    def to_dict(self):
        return {
            "payment_id": str(self.payment_id),
            "bank_name" : self.bank_name,
            "bank_account_no" : self.bank_account_no,
            "total_price": self.total_price,
            "referral_code": str(self.referral_code),
            "status": self.status,
        }
