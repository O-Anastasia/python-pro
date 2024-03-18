#Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.

def progr(a, q, n):
    for _ in range(n):
        yield a
        a *= q

for item in progr(2,3,5):
    print(item)
        
