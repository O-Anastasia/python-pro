from user_exception_1 import IncorrectPrice
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

class Dish:
    def __init__(self, name, price : int | float):
        if not isinstance(price, int | float):
            logger.error('Price is not a number')
            raise TypeError('Price must be a number')
        if price <= 0:
            logger.error('Price is not positive')
            raise IncorrectPrice('Price must be above zero') 
        self.name = name
        self.price = price
        logger.info(f'New dish {self.name} was created')

dish_1 = Dish(name="Pizza", price=12.5)
dish_2 = Dish(name="Pasta", price=8)
dish_3 = Dish(name="Salad", price=5.5)
dish_4 = Dish(name="Soup", price=4.5)
dish_5 = Dish(name="Steak", price=15)
dish_6 = Dish(name="Fish", price=10)
dish_7 = Dish(name="Sushi", price=20)
