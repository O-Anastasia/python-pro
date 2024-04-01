# Task 4
# Створіть абстрактний базовий клас "Фігура" і від нього успадкуйте конкретні класи,
# такі як "Коло", "Прямокутник", "Трикутник" і т.д. Кожен клас має мати методи для обчислення
# площі та периметру фігури. 
# Створіть декілька об'єктів різних фігур і виведіть їх площу та периметр.

from abc import ABC, abstractmethod

class Figure(ABC):
    
    @abstractmethod
    def square(self):
        ...
    @abstractmethod
    def perimetr(self):
        ...     

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return 3.14 * self.radius ** 2
    
    def perimetr(self):
        return 3.14 * self.radius
    
class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)
    

class Triangle(Figure):

    def __init__(self, length_1, height, length_2, length_3):
        self.length_1 = length_1
        self.height = height
        self.length_2 = length_2
        self.length_3 = length_3 

    def square(self):
        return 0.5 * self.length_1 * self.height
    
    def perimetr(self):
        return self.length_1 + self.length_2 + self.length_3
            


figures = [Circle(5), Rectangle(3, 7), Triangle(3, 2, 5, 7)]


for figure in figures:
    print(figure.square())

for figure in figures:
    print(figure.perimetr())


