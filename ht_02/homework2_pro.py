import dataclasses


@dataclasses.dataclass
class Dish:
    name: str
    price: float | int


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))


class Menu:
    def __init__(self, name: str):
        self.name = name
        self.__categories = []

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__categories))
    

class Discount:
    def client_discount(self):
        return 1

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
        
    def total_order(self):
        total = 0
        for dish, quantity in zip(self.__order, self.__quantity):
            total += dish.price * quantity
        return total
    

class Client:
    def __init__(self, name, discount : Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        return order.total_order() * self.discount.client_discount()

    def __str__(self):
        return f'{self.name}, your discount is {self.discount}'
    
        

dish_1 = Dish(name="Pizza", price=12.5)
dish_2 = Dish(name="Pasta", price=8)
dish_3 = Dish(name="Salad", price=5.5)
dish_4 = Dish(name="Soup", price=4.5)
dish_5 = Dish(name="Steak", price=15)
dish_6 = Dish(name="Fish", price=10)
dish_7 = Dish(name="Sushi", price=20)

discount_1 = GoldDiscount()
client_1 = Client('John', discount_1)
order_1 = Order()

order_1.make_order(dish_1, 2)
order_1.make_order(dish_2, 2)
order_1.make_order(dish_3)
order_1.make_order(dish_4)

print(f'{client_1.get_total_price(order_1)} UAH')



print(client_1)


# Решение учителя:


import dataclasses
import uuid


class Discount:

    def discount(self):
        return 0


class SilverDiscount(Discount):

    def discount(self):
        return 5


class GoldDiscount(Discount):

    def discount(self):
        return 10


@dataclasses.dataclass
class Dish:
    name: str
    price: float | int


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.__dishes))


class Menu:
    def __init__(self):
        self.__categories = []

    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return '\n'.join(map(str, self.__categories))


class Order:
    def __init__(self, discount: Discount):
        self.id = uuid.uuid4()
        self.__dishes = []
        self.__quantities = []
        self.discount = discount

    def add_dish(self, dish: Dish, quantity: int = 1):
        self.__dishes.append(dish)
        self.__quantities.append(quantity)

    def total_price(self):
        total = 0
        for dish, quantity in zip(self.__dishes, self.__quantities):
            total += dish.price * quantity
        return total * (1 - self.discount.discount() / 100)

    def __str__(self):
        return '\n'.join([f'{dish.name}x{quantity}={dish.price * quantity}' for dish, quantity in zip(self.__dishes, self.__quantities)])
# Тут в return используется генератор списка: оператором for распаковывается кортеж dish, quantity после функции zip.
# К этим кортежам применяется выражение, которое стоит перед for. Получается новый список,
# к которому применяется метод join 

if __name__ == '__main__':
    dish1 = Dish('Pizza', 10)
    dish2 = Dish('Pasta', 8)
    dish3 = Dish('Salad', 5)
    dish4 = Dish('Burger', 7)

    category1 = Category('Italian')
    category1.add_dish(dish1)
    category1.add_dish(dish2)
    category2 = Category('American')
    category2.add_dish(dish3)
    category2.add_dish(dish4)

    menu = Menu()
    menu.add_category(category1)
    menu.add_category(category2)

    discount = GoldDiscount()
    order = Order(discount)
  
    order.add_dish(dish1, 1)
    print(order.total_price())
