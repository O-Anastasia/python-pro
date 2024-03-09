#Task1
# Для попереднього проєкту (Замовлення продуктів в магазині) 
# реалізувати можливість поєднання двох кошиків в один за допомогою оператора "+=".
from user_exception import IncorrectPrice
from products import Product
from cart import Cart

if __name__ == '__main__':
    try:
        product1 = Product('Milk', 25)
        product2 = Product('Bread', 10)
        product3 = Product('Eggs', 20)  
        product4 = Product('meat', 1)
        cart = Cart()

        cart.add_product(product1, 5)
        cart.add_product(product2)
        cart.add_product(product3, 3)
        
        print(cart)

        cart1 = Cart()
        cart1.add_product(product1, 1)
        cart1.add_product(product2, 2)
        cart2 = Cart()
        cart2.add_product(product3, 1)
        cart2.add_product(product4, 2)

        cart1 += cart2
        print(cart1)

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