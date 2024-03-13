class Payment:
    def __init__(self, payment_id, amount, payment_date, payment_method):
        self._payment_id = payment_id
        self._amount = amount
        self._payment_date = payment_date
        self._payment_method = payment_method

    @property
    def payment_id(self):
        return self._payment_id

    @property
    def amount(self):
        return self._amount

    @property
    def payment_date(self):
        return self._payment_date

    @property
    def payment_method(self):
        return self._payment_method