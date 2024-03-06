#Task1. Модифікуйте перше домашнє завдання (Про замовлення), додавши перевірки в методи класів, 
# логування подій та обробку виключних ситуацій.
# При спробі встановити від'ємну або нульову вартість товару треба викликати виняткову ситуацію, тип якої реалізувати самостійно.
class IncorrectPrice(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f'{self.message}: '

class Product:
    def __init__(self, name, price : int | float):
        if not isinstance(price, int | float):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise IncorrectPrice('Price must be above zero') 
        self.name = name
        self.price = price
            
    def __str__(self):
        return f'{self.name.title()}: {self.price} UAH'


class Cart:
    def __init__(self):
        self.__products = []
        self.__quantity = []
    
    def add_product(self, product : Product, quantity : int | float = 1):
        if not isinstance(product, Product):
            raise TypeError('Product must be from type product')
        if not isinstance(quantity, int | float):
            raise TypeError('Quantity of products to add must be a number')
        if quantity <=0:
            raise ValueError('Quantity of products to add must be above zero')
        
        self.__products.append(product)
        self.__quantity.append(quantity)


    def remove_product(self, product : Product, quantity : int | float = 1):
        if not isinstance(product, Product):
            raise TypeError('Product must be from type product')
        if not isinstance(quantity, int | float):
            raise TypeError('Quantity of products to remove must be a number')
        if quantity <=0:
            raise ValueError('Quantity of products to remove must be above zero')

        if product in self.__products: 
            index = self.__products.index(product) 
            self.__quantity[index] = self.__quantity[index] - quantity 
            if self.__quantity[index] <= 0:  
                del self.__products[index]
                del self.__quantity[index] 

    def total(self):
        total = 0
        for product, quantity in zip(self.__products, self.__quantity):
            total += product.price * quantity
        return total

    def __str__(self):
        if not self.__products:
            return 'Cart is empty'
        return '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                             zip(self.__products, self.__quantity))) +\
               f'\nTotal: {self.total()} UAH'


if __name__ == '__main__':
    try:
        product1 = Product('Milk', 25)
        product2 = Product('Bread', 10)
        product3 = Product('Eggs', 20)  
        cart = Cart()
        cart.add_product(product1, 5)
        cart.add_product(product2)
        cart.add_product(product3, 3)
        cart.remove_product(product1, 0)
        print(cart)  
    except Exception as e:
        print(e)     

#Task 2
# Модифікуйте друге домашнє завдання (Дисконт),
# додавши перевірки в методи класів, логування подій та обробку виключних ситуацій.
# При спробі встановити знижку не в межах 0-100 % треба викликати виняткову ситуацію, 
#тип якої реалізувати самостійно.     

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
    

class IncorrectDiscount(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}: '


class Discount:
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
        
    def total_order(self):
        total = 0
        for dish, quantity in zip(self.__order, self.__quantity):
            total += dish.price * quantity
        return total
    

class Client:
    def __init__(self, name, discount : Discount):
        if discount.client_discount() < 0 or discount.client_discount() > 1:
            raise IncorrectDiscount('Discount must be in diapason from 0 to 1') 
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

if __name__ == '__main__':
    try:
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
    except IncorrectDiscount as e:
        print(e)


# Решение учителя. Тут надо прописать все возможные ошибки в  базовом классе Discount.
# Метод raise NotImplemented означает то, что надо его переопределить в дочернем классе обязательно.
        
class Discount:
    def __init__(self, value : int | float):
        if not isinstance(value, int | float):
            raise TypeError("Value must be a number")
        if not 0 < value < 1:
            raise ValueError('Value must be in range from 0 to 1')
        self._value = value
    
    def method(self):
        raise NotImplemented('Subclass must implement this method')
    

class RegularDiscount(Discount):
    def __init__(self, value : int | float = 0.95):
        super().__init__(value)
        self._value = value

    def method(self):
        return self._value        
        
class SilverDiscount(Discount):
    def __init__(self, value : int | float = 0.87):
        super().__init__(value)
        self._value = value

    def method(self):
        return self._value

x = RegularDiscount()
print(x.method())            


        