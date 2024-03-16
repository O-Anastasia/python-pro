from user_exception_1 import IncorrectPrice
from user_exception_2 import IncorrectDiscount
from discount import Discount, GoldDiscount, SilverDiscount, RegularDiscount, InvalidDiscount
from order import Order
from dish import Dish
from order import Order
from menu import Menu
from category import Category
from client import Client
from orderiterator import OrderIterator


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

        client_1 = Client('John', discount_2)
        order_1 = Order()
        order_1.make_order(dish_1, 2)
        order_1.make_order(dish_2, 2)
        order_1.make_order(dish_3)
        order_1.make_order(dish_4)

        order_2 = Order()
        order_2.make_order(dish_5)
        order_2.make_order(dish_7)

        order_1 += order_2
        print(order_1)
        print(len(order_1))
        print(order_1[0])

        for dish, quantity in order_1:
            print(dish, quantity)

        print(f'{client_1.get_total_price(order_1)} UAH')
        print(client_1)
    except Exception as e:
        print(e)
