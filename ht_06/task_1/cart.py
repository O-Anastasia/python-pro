from products import Product
from cartiterator import CartIterator


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

    def __iter__(self):
        return CartIterator(self.__products, self.__quantity)

    def __iadd__(self,other):
        if not isinstance(other, Cart):
            return NotImplemented
        for product, quantity in zip(other.__products, other.__quantity):
            self.add_product(product,quantity)
        return self

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




