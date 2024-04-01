# Task 2
# Створіть клас "Користувач", який має властивості first_name і last_name. 
# Використайте декоратори @property для забезпечення доступу до цих властивостей. 
# Визначте метод __setattr__, який забороняє безпосередню зміну значень first_name і last_name. 
# Використовуйте метод __getattr__, який повертає повідомлення про те, що властивість не існує, 
# якщо спробувати отримати доступ до неіснуючої властивості. 
# Створіть об'єкт користувача і спробуйте змінити значення first_name 
# та отримати доступ до неіснуючої властивості.

class User:

    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str):
            raise TypeError(f'First name must be a string')
        if not isinstance(last_name, str):
            raise TypeError(f'Last name must be a string')
        
        self.__dict__['first_name'] = first_name
        self.__dict__['last_name'] = last_name

    @property
    def first_name(self):
        return self.__dict__['first_name']

    @property
    def last_name(self):
        return self.__dict__['last_name']    
    
    def __setattr__(self, key, value):
        if key in ('first_name', 'last_name'):
            raise NameError(f'You can not change this attributes')
        
    def __getattr__(self, item):
        return f'There is no such attribute'
    
x = User('John', 'Doe')
print(x.first_name)
print(x.last_name)
#x.first_name = 'Anna'
print(x.age)

        