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


class Discount:
    def __init__(self):
        logger.debug(f'{self.__class__.__name__} created.')

    def client_discount(self):
        return 1

    def __str__(self):
        return f'{self.client_discount()}'


class InvalidDiscount(Discount):        
    def client_discount(self):
        return 1.1
    
    def __str__(self):
        return f'{self.client_discount()}'
    

class RegularDiscount(Discount):        
    def client_discount(self):
        return 0.95
    
    def __str__(self):
        return f'{self.client_discount()}'


class SilverDiscount(Discount):
    def client_discount(self):
        return 0.87    

    def __str__(self):
       return f'{self.client_discount()}'


class GoldDiscount(Discount):
    def client_discount(self):
        return 0.80
    
    def __str__(self):
        return f'{self.client_discount()}'