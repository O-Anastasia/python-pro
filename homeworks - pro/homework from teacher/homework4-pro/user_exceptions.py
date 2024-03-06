class PriceError(Exception):
    def __init__(self, price):
        self.price = price
        super().__init__(f"Price {price} is invalid")