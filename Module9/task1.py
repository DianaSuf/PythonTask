# Сумма чисел 2
with open('numbers.txt', 'r') as numbers, open('answerd.txt', 'w') as answer:
    summ = sum(int(line.strip()) for line in numbers)
    print("Содержимое файла numbers.txt:")
    numbers.seek(0)
    print(numbers.read(), end='')
    answer.write(str(summ))
    print("\nСодержимое файла answer.txt:")
    print(summ)