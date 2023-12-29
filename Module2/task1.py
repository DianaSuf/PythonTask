# Генерация списка
N = int(input("Введите число: "))
def get_odd_list(N):
    return list(range(1, N + 1, 2))
print("Список из нечётных чисел от одного до N: ", get_odd_list(N))