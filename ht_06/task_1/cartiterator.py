class CartIterator:

    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__product):
            product = self.__product[self.__index]
            quantity = self.__quantity[self.__index]
            self.__index += 1
            return(product, quantity)
    
        raise StopIteration