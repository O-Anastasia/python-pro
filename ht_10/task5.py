# Task 5
# Створіть абстрактний базовий клас "ПлатіжнийЗасіб" з методом "здійснити_платіж()". 
# Створіть підкласи "КредитнаКарта", "БанківськийПереказ", "ЕлектроннийГаманець" і т.д., 
# які успадковують цей метод та реалізовують його відповідно до специфіки кожного платіжного засобу.
# Створіть клас "ПлатіжнийПроцесор", який містить список доступних платіжних засобів 
# та метод для виконання платежу через вибраний засіб. 
# Можна створити об'єкти різних платіжних засобів, додати їх до платіжного процесора 
# і здійснити платежі через них.

from abc import ABC, abstractmethod

class PaymentWay(ABC):

    @abstractmethod
    def make_payment(self):
        pass
    

class CreditPayment(PaymentWay):

    def __init__(self, security_code):
        self.security_code = security_code

    def make_payment(self):
        print(f'Varifing security code: {self.security_code}')


class DebitPayment(PaymentWay):

    def __init__(self, security_code):
       self.security_code = security_code

    def make_payment(self):
        print(f'Varifing security code: {self.security_code}')

class E_Wallet(PaymentWay):

    def __init__(self, card_number):
       self.card_number = card_number

    def make_payment(self):
        print(f'Varifing security code: {self.card_number}')

class PaymentProcessor:
    ...