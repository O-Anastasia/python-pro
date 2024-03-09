from user_exception_2 import IncorrectDiscount
from discount import Discount
from order import Order

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


class Client:
    def __init__(self, name, discount : Discount):
        if not isinstance(discount, Discount):
            logger.error('Item is not from class Discount')
            raise TypeError('Discount must be class Discount')
        if discount.client_discount() < 0 or discount.client_discount() > 1:
            logger.error('Discount is not in range from 0 to 1')
            raise IncorrectDiscount('Discount must be in range from 0 to 1') 
        
        self.name = name
        self.discount = discount
        logger.debug(f'New client: {self.name} appeared')

    def get_total_price(self, order : Order):
        logger.debug('Total order with discount was counted')
        return order.total_order() * self.discount.client_discount()

    def __str__(self):
        return f'{self.name}, your discount is {self.discount}'