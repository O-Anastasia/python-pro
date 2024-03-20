# Task 2
# Реалізуйте свій аналог генераторної функції range().
def my_range(*args):
    start, stop, step = 0, None, 1 
    
    if len(args) == 1:
        stop = args[0]
        if not isinstance(stop, int):
            raise TypeError('start must be a number')
    elif len(args) == 2:
        start, stop = args
        if not isinstance(start, int):
            raise TypeError('start must be a number')
        if not isinstance(stop, int):
            raise TypeError('stop must be a number') 
    elif len(args) == 3:
        start, stop, step = args
        if not isinstance(step, int):
            raise TypeError('step must be a number')
        if not isinstance(start, int):
            raise TypeError('start must be a number')
        if not isinstance(stop, int):
            raise TypeError('stop must be a number')
    else:
        TypeError('my_range expect 1 or 2 or 3 arguments')   
    
    if step == 0:
        raise ValueError('Step must not be 0')
    if step < 0:
        while start > stop:
            yield start
            start += step
    else:
        while start < stop:
            yield start
            start += step

for item in my_range(1,'mhgf',2):
    print(item)
