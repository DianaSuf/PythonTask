# Генерация
n = int(input("Введите длину списка: "))
print([(1 if i % 2 == 0 else i % 5) for i in range(n)])