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

class Category:
    
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []
        logger.info(f'New category {self.name} was created')

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))
