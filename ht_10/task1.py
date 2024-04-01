# Task 1
# Створіть клас "Рахунок", який має приватну властивість "баланс". 
# Використайте дескриптор для реалізації контролю доступу до цієї властивості. 
# Додайте властивість balance з декоратором @property, яка повертає значення балансу. 
# Визначте метод __setattr__, який забороняє безпосереднє змінення значення балансу. 
# Також визначте метод __getattr__, який повертає повідомлення про те, що властивість не існує, 
# якщо доступ до неї спробувати отримати. 
# Використовуйте цей клас для створення об'єкту рахунку
# та спробуйте змінити значення балансу та отримати доступ до неіснуючої властивості.

class AccountDescriptor:

    def __init__(self, attribute):

        self.attribute = attribute

    def __get__(self, instance, owner):
        value = instance.__dict__.get(self.attribute)
        return value

    def __set__(self, instance, value):               
        raise ValueError(f'Balance must not be changed')
          

    def __del__(self):
        raise AttributeError(f'You must not delete balance')

class Account:

    def __init__(self, balance):
        if not isinstance(balance, int | float):
            raise TypeError(f'Balance must be a number')
        self.__dict__['balance'] = balance

    balance = AccountDescriptor('balance')

x = Account('hgfjhgf')
print(x.balance)
x.balance = 5500
print(x.balance)





