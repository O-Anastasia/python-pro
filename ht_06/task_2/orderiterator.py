class OrderIterator:

    def __init__(self, dishes, quantity):
        self.__dishes = dishes
        self.__quantity = quantity
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__dishes):
            dishes = self.__dishes[self.__index]
            quantity = self.__quantity[self.__index]
            self.__index += 1
            return(dishes, quantity)
    
        raise StopIteration