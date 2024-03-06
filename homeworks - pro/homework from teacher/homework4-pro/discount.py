class Discount:

    def __init__(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Discount must be a number")
        if not 0 <= value <= 1:
            raise ValueError("Discount must be between 0 and 1")

        self.__value = value

    def discount(self):
        return self.__value


class GoldDiscount(Discount):
    def __init__(self, value=0.1):
        super().__init__(value)


class SilverDiscount(Discount):
    def __init__(self, value=0.2):
        super().__init__(value)

