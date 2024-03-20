# Реалізуйте генераторну функцію для генерації послідовності дат. 
# Початкова та кінцеві дати мають бути задані параметрами цієї функції.

import datetime


def gen_date_range(start_date: str, end_date: str, step: int):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    step = datetime.timedelta(days=step)

    while start_date < end_date:
        yield start_date.strftime('%Y-%m-%d')
        start_date += step


for date in gen_date_range('2024-02-01', '2024-04-01', 3):
    print(date)

    