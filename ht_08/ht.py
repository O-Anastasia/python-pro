# Task 1
# Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
# і поверне суми елементів отриманого списку.

import random

def my_sqrt(number):
    return number ** 2

def new_list(sequence, func):
    return sum(func(element) for element in sequence)

x = [random.randint(1, 10) for _ in range(10)]
print(new_list(x,my_sqrt))


# Task 2
# Напишіть декоратор, який зберігає результати обчислення функції
# у файл для подальшого використання.

def save_results(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'a') as file:
                file.write(f'Function {func.__name__} has arguments {args} and {kwargs}: {result}\n')
            return result
        return wrapper
    return decorator


@save_results('log.txt')
def signiture(first_name, last_name):
    return f'{first_name.title()} {last_name.title()}'

print(signiture('kate', 'sidorova'))


# Task 3
# Напишіть декоратор, який вимірює час виконання функції.

import time

def time_measure(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            with open(file_name, 'a') as file:
                file.write(f'Function {func.__name__} was executed in {end - start} seconds: {result}\n')
            return result
        return wrapper
    return decorator


@time_measure('log.txt')
def fibonacci(n):
    a, b = 0, 1
    sequance = []
    for _ in range(n): 
        a, b = b, a + b
        sequance.append(a)
    time.sleep(4)    
    return sequance
       
print(fibonacci(10))

# Task 4
# Напишіть декоратор, який обмежує кількість викликів функції

def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls < max_calls:
                wrapper.calls +=1
                return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator    

@limit_calls(2)
def person_name(first_name, last_name):
    return f"Person's name is {first_name} {last_name}" 

print(person_name('John', 'Black'))
print(person_name('Kate', 'White'))
print(person_name('Ann', 'Red'))
print(person_name('Jack', 'Smith'))

# Task 5
# Напишіть декоратор, який кешує результати обчислення функції 
# і повертає їх з кешу при наступних викликах з тими самими аргументами.
def cash_decorator(func):
    cash = {}
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cash:
             cash[key] = func(*args, **kwargs)
        return cash[key]
    return wrapper

@cash_decorator
def sum(a, b, c = 3, d = 5):
    return a + b + c + d

print(sum(3, 7, c = 2, d = 9))
print(sum(3, 7, d = 9, c = 2))