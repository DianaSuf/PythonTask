# Страшный код
first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]
first_list.extend(second_list)
count_5 = first_list.count(5)
print("Количество цифр 5 при первом объединении: ", count_5)

while 5 in first_list:
    first_list.remove(5)

first_list.extend(third_list)
count_3 = first_list.count(3)
print("Количество цифр 3 при втором объединении: ", count_3)
print("Итоговый список:", first_list)