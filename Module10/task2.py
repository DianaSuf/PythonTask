# Счастливое число
import random

def write_to_file(number):
    with open('out_file.txt', 'a') as f:
        f.write(str(number) + '\n')

def request_numbers():
    total = 0
    while total < 777:
        try:
            number = int(input("Введите число: "))
            if random.randint(1, 13) == 1:
                raise Exception("Вас постигла неудача!")
            total += number
            write_to_file(number)
        except Exception as e:
            print(str(e))
            break
    if total >= 777:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")

request_numbers()