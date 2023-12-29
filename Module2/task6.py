# Бегущие цифры
offset_count = int(input("Cдвиг: "))
list_of_numbers = input("Изначальный список: ").split()
print(list_of_numbers)
result = list_of_numbers[-offset_count:] + list_of_numbers[:-offset_count]
print("Сдвинутый список:", " ".join(result))