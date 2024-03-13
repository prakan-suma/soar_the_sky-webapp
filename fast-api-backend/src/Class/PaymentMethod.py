class PaymentMethod:
    def __init__(self, method_type, method_provider, method_details):
        self._method_type = method_type
        self._method_provider = method_provider
        self._method_details = method_details

    @property
    def method_type(self):
        return self._method_type

    @property
    def method_provider(self):
        return self._method_provider

    @property
    def method_details(self):
        return self._method_details