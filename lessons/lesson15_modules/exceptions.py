class InvalidPriceException(Exception):
    def __init__(self, price, message):
        self.price = price
        self.message = message
        super().__init__(message)