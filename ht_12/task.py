# Task1
# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, 
# що складаються з однієї літери R, за якою слідує одна або більше літер b, за якою одна r. 
# Враховувати верхній та нижній регістр.

r'^Rb+r$'

# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re

def valid(string):
    pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'
    if re.match(pattern, string):
        print('Inputed card number is ok')
    else:
        print('Inputed cardnumber is not valid')

string1 = '1111-2222-3333-4444'
valid(string1)       

# Task 3
# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

def check_mail(string):
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_]*-?[a-zA-Z0-9_]*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'
    if re.match(pattern, string):
        print('Inputed mail is ok')
    else:
        print('Inputed mail is not valid')

email = '1111222233334444-@gmail.com'
check_mail(email)       


# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. 
# Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.

def check_login(string):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    if re.match(pattern, string):
        print('Inputed login is ok')
    else:
        print('Inputed login is incorrect')

login = 'Anastasiya'
check_login(login)       