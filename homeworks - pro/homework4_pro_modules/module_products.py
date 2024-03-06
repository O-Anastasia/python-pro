from module_exception import IncorrectPrice

class Product:
    
    def __init__(self, name, price : int | float):
        if not isinstance(price, int | float):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise IncorrectPrice(price) 
        
        self.name = name
        self.price = price
            
    def __str__(self):
        return f'{self.name.title()}: {self.price} UAH'

x = Product('pizza', 3)
print(x)