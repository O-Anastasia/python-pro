# Task 1
# Створіть клас Product для опису товару. У якості атрибутів товару можна використовувати назву, цінц та опис товару. Створіть декілька інстансів класу Product.
# Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. Кошик може містити декілька товарів певної кількості. Реалізуйте метод обчислення вартості кошика.
# В усіх класах має бути визначений метод str.
#Задача№1 через 2 списка
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name.title()}: {self.price} UAH'



class Cart:

    def __init__(self):
        self.__products = []
        self.__quantity = []
    
    def add_product(self, product : Product, quantity : int | float = 1):
        self.__products.append(product)
        self.__quantity.append(quantity)
# Если мы захотим убрать из корзины продукты, создаем этот метод:
# В переменных указываем класс продукты и количесвто.
    def remove_product(self, product : Product, quantity : int | float = 1): # В переменных указываем класс продукты и количесвто.
        if product in self.__products: # Условие: если такой продукт есть в нашем списке, заходим в этот цикл 
            index = self.__products.index(product) # Находим индекс  этого продукта
            self.__quantity[index] = self.__quantity[index] - quantity # По индексу из списка количества удаляем его количество( взятое из аргументов)
            if self.__quantity[index] <= 0: # Если после разности (выше) количество этого продукта отриц или = 0:  
                del self.__products[index] # Удаляем это продукт из обоих списков
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
    product1 = Product('Milk', 25)
    product2 = Product('Bread', 10)
    product3 = Product('Eggs', 20)

    cart = Cart()
    cart.add_product(product1, 2)
    cart.add_product(product2)
    cart.add_product(product3, 3)
    print(cart)

#Задача№1 через словарь
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name.title()}: {self.price} UAH'



class Cart:
# в словаре ключами будут продукты, значениями - количество
    def __init__(self):
        self.__products = {}
      
# Если в словаре продуктов(где продукты - это ключи) есть такой продукт, то по ключу этого продукта добавить 
# к нему еще quantity. Если такого продукта не было в словаре, то вернется О. И к нему добавим quantity     
    def add_product(self, product : Product, quantity : int | float = 1):
        self.__products[product] = self.__products.get(product, 0) + quantity

# Если мы захотим убрать из корзины продукты, создаем этот метод:
# В переменных указываем класс продукты и количесвто.
    def remove_product(self, product : Product, quantity : int | float = 1): 
        if product in self.__products: # Условие: если такой продукт есть в нашем списке, заходим в этот цикл 
            self.__products[product]= self.__products[product] - quantity # По ключу[product] удаляем количество( взятое из аргументов)
            if self.__quantity[product] <= 0: # Если после разности (выше) количество этого продукта отриц или = 0:  
                del self.__products[product] # Удаляем это продукт из словаря
                

# Создаем метод подсчета общей стоимости:
    def total(self):
        total = 0
        for product, quantity in self.__products.items():
            total = total + product.price * quantity
        return total

    def __str__(self):
        if not self.__products:
            return 'Cart is empty'
        return '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                             self.__products.items())) +\
               f'\nTotal: {self.total()} UAH'

if __name__ == '__main__':
    product1 = Product('banana', 5)
    product2 = Product('orange', 3)
    product3 = Product('milk', 8)

    cart = Cart()
    cart.add_product(product1, 4)
    cart.add_product(product2)
    cart.add_product(product3, 5)
    print(cart)

# Task 2
# Необхідно розробити Python-скрипт, який буде повертати користувачеві меню ресторану. Зазвичай, меню ресторану містить наступні елементи:
# - Категорії страв (наприклад, закуски, основні страви, десерти).
# - Страви у кожній категорії.
# Основні класи, які необхідно створити для реалізації меню ресторану:
# Клас Страва: відповідає за збереження інформації про окрему страву, включаючи її назву, опис та ціну.
# Клас Категорія страв: відповідає за збереження страв, які належать до конкретної категорії. Включає список об'єктів "Страва".

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


dish_1 = Dish(name="Pizza", price=12.5)
dish_2 = Dish(name="Pasta", price=8)
dish_3 = Dish(name="Salad", price=5.5)
dish_4 = Dish(name="Soup", price=4.5)
dish_5 = Dish(name="Steak", price=15)
dish_6 = Dish(name="Fish", price=10)
dish_7 = Dish(name="Sushi", price=20)


category_1 = Category(name="Main Course")
category_2 = Category(name="Appetizer")

category_1.add_dish(dish_1)
category_1.add_dish(dish_2)
category_1.add_dish(dish_3)
category_2.add_dish(dish_4)
category_2.add_dish(dish_5)
category_2.add_dish(dish_6)
category_2.add_dish(dish_7)

menu = Menu(name="Restaurant Menu")
menu.add_category(category_1)
menu.add_category(category_2)

print(menu)

#Это задача - матрешка. С начала создается самый мелкий предмет: блюдо, затем категория, затем меню.
# Блюдо добавляется методом add_dishes в список (категорию). А категория методом add_category в список(меню) 







