# Task 1
# Створіть клас "Рахунок", який має приватну властивість "баланс". 
# Використайте дескриптор для реалізації контролю доступу до цієї властивості. 
# Додайте властивість balance з декоратором @property, яка повертає значення балансу. 
# Визначте метод __setattr__, який забороняє безпосереднє змінення значення балансу. 
# Також визначте метод __getattr__, який повертає повідомлення про те, що властивість не існує, 
# якщо доступ до неї спробувати отримати. 
# Використовуйте цей клас для створення об'єкту рахунку
# та спробуйте змінити значення балансу та отримати доступ до неіснуючої властивості.
class Account:

    def __init__(self, balance):
        if not isinstance(balance, int | float):
            raise TypeError(f'Balance must be a number')
        self.__dict__['balance'] = balance

    @property
    def balance(self):
        value = self.__dict__['balance']
        return value   
    
    def __setattr__(self, key, value):
        if key in ('balance'):
            raise ValueError(f'You can not change balance')
        
    def __getattr__(self, item):
        return f'There is no such attribute'   
    
x = Account(5000)
#x.balance = 5500

#print(x.balance)

print(x.type)