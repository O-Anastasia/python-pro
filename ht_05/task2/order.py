from dish import Dish
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

class Order:
    
    def __init__(self):
        self.__order = []
        self.__quantity = []

    def make_order(self, dish : Dish, quantity : int = 1):
        self.__order.append(dish)
        self.__quantity.append(quantity)
        logger.debug('New order was created')

    def __iadd__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        for dish, quantity in zip(other.__order, other.__quantity):
            self.make_order(dish, quantity)    
        return self
    
    def total_order(self):
        total = 0
        for dish, quantity in zip(self.__order, self.__quantity):
            total += dish.price * quantity
        logger.debug('Total order was counted')    
        return total
    
    def __str__(self):
        return f'your order is {self.total_order()}'



