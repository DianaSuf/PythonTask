# Обратный анализ чётных чисел
numbers = [int(x) for x in input().split()]
even_numbers = []
index = len(numbers) - 1

while index >= 0:
    if numbers[index] % 2 == 0:
        even_numbers.append(numbers[index])
    index -= 1

for number in even_numbers:
    print(number, end=' ')