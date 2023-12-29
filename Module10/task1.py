# Имена 2
with open('people.txt', 'r') as file:
    total_chars = 0
    line_number = 1
    for line in file:
        if len(line.strip()) < 3:
            print(f'Ошибка: менее трёх символов в строке {line_number}.')
        else:
            total_chars += len(line.strip())
        line_number += 1
    print(f'Общее количество символов: {total_chars}.')