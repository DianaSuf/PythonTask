# Считалка
humans = [i + 1 for i in range(int(input("Количество человек: ")))]
offset = int(input("Какое число в считалке? "))
index = 0

while len(humans) > 1:
    print("Текущий круг людей: ", humans)
    print("Начало счёта с номера, ", humans[index])
    current_index = (index + offset - 1) % len(humans)
    print("Выбывает человек под номером ", humans[current_index])
    humans.remove(humans[current_index])
    index = current_index % len(humans)

print("Остался человек под номером ", humans[0])