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

tmp = (item for item in range(n + 1) if is_prime(item)) 
print(list(tmp))


def gen_prime_numbers(n):
    for n in range(2, n + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n


print(*gen_prime_numbers(100))
