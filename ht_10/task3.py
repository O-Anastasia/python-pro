# Task 3
# Створіть клас "Прямокутник", який має приватні властивості width і height. 
# Використайте декоратори @property для створення властивостей width і height, 
# які повертають значення цих властивостей. 
# Визначте метод __setattr__, який забороняє безпосередню зміну значень width і height. 
# Використовуйте метод __getattr__, який повертає повідомлення про те, 
# що властивість не існує, якщо спробувати отримати доступ до неіснуючої властивості. 
# Додайте метод area, який обчислює площу прямокутника. 
# Створіть об'єкт прямокутника і спробуйте змінити значення width і height, 
# а також отримати доступ до неіснуючої властивості та обчислити площу прямокутника.


class Rectangle:

    def __init__(self, width, height):
        if not isinstance(width, int | float):
            raise TypeError(f'Width must be a number')
        if not isinstance(height, int | float):
            raise TypeError(height, int | float)

        self.__dict__['width'] = width
        self.__dict__['height'] = height

    @property
    def width(self):
        return self.__dict__['width']
    
    @property
    def height(self):
        return self.__dict__['height']
        
    def __setattr__(self, key, value):
        if key in ('width', 'height'):
            raise NameError(f'You can not change this attribute')
        
    def __getattr__(self, item):
        return f'There is no such attribute'
        
    def area(self):
        return self.__dict__['width'] * self.__dict__['height'] 
    


x = Rectangle(5, 6)
print(x.area())
print(x.width)
print(x.lenth)





        



