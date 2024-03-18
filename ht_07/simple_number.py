# Task 3
# Напишіть генераторну функцію, яка повертатиме прості числа. 
# Верхня межа діапазону повинна бути задана параметром цієї функції.
def is_prime(number):
    if number < 2:
        return False
    index = 2
    while index <=  number ** 0.5:
        if number % index == 0:
            return False
        index += 1
    return True


n = int(input('Input number: '))
my_list = list(range(n + 1))

tmp = [item for item in my_list if is_prime(item)] 

print(tmp)

