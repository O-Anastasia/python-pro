# Task 1
# Реалізувати логування подій у класах, 
# які використовували під час вирішення попередніх завдань (про замовлення, меню). 
# Переконайтеся у працездатності проекту.

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

class IncorrectPrice(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'{self.message}: '

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

class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []
        logger.info(f'New category {self.name} was created')

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))


class Menu:
    def __init__(self, name: str):
        self.name = name
        self.__categories = []
        logger.info(f'New menu {self.name} was created')

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__categories))
    

class IncorrectDiscount(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}: '


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


class Order:
    def __init__(self):
        self.__order = []
        self.__quantity = []

    def make_order(self, dish : Dish, quantity : int = 1):
        self.__order.append(dish)
        self.__quantity.append(quantity)
        logger.debug('New order was created')
        
    def total_order(self):
        total = 0
        for dish, quantity in zip(self.__order, self.__quantity):
            total += dish.price * quantity
        logger.debug('Total order was counted')    
        return total
    

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

    def get_total_price(self, order):
        logger.debug('Total order with discount was counted')
        return order.total_order() * self.discount.client_discount()

    def __str__(self):
        return f'{self.name}, your discount is {self.discount}'
    
    

if __name__ == '__main__':
    try:
        dish_1 = Dish(name="Pizza", price=12.5)
        dish_2 = Dish(name="Pasta", price=8)
        dish_3 = Dish(name="Salad", price=5.5)
        dish_4 = Dish(name="Soup", price=4.5)
        dish_5 = Dish(name="Steak", price=15)
        dish_6 = Dish(name="Fish", price=10)
        dish_7 = Dish(name="Sushi", price=20)

        discount_1 = GoldDiscount()
        discount_2 = SilverDiscount()
        discount_3 = RegularDiscount()
        discount_4 = InvalidDiscount()

        client_1 = Client('John', discount_4)
        order_1 = Order()
        order_1.make_order(dish_1, 2)
        order_1.make_order(dish_2, 2)
        order_1.make_order(dish_3)
        order_1.make_order(dish_4)

        print(f'{client_1.get_total_price(order_1)} UAH')
        print(client_1)
    except Exception as e:
        print(e)
