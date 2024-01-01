from exceptions import InvalidPriceException

class Product:
    """
    Product class.
    """
    def __init__(self, name: str, price: float | int):
        self.name = name
        if price <= 0:
            raise InvalidPriceException(price, 'Zero or negative price was attempted to set')
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"
