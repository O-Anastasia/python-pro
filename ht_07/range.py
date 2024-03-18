# Task 2
# Реалізуйте свій аналог генераторної функції range().
def my_range(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for item in my_range(2,10,2):
    print(item)
