from user_exceptions import PriceError


class Product:

    def __init__(self, name, price):
        if not isinstance(price, int | float):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise PriceError(price)

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"