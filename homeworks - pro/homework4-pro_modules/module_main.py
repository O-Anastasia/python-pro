from module_exception import IncorrectPrice
from module_products import Product
from module_cart import Cart

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

    except IncorrectPrice as ie:
        print(f'Incorrect price: {ie}')
    except TypeError as te:
        print(f'Type error: {te}')
    except ValueError as ve:
        print(f'Value error: {ve}')
    except Exception as e:
        print(f'Exception: {e}')
    finally:
        print('Done')     