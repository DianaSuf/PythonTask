# Телефонные номера
import re

numbers = ['9999999999', '999999-999', '99999x9999']

for number in numbers:
    if re.match(r'^[89]\d{9}$', number):
        print(f'{number}: всё в порядке')
    else:
        print(f'{number}: не подходит')