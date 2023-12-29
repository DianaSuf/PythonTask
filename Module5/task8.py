# Бегущая строка
def find_cyclic_offset(first_string, second_string):
    if len(first_string) != len(second_string):
        return "Первую строку нельзя получить из второй с помощью циклического сдвига."
    for offset in range(len(first_string)):
        offset_string = second_string[-offset:] + second_string[:-offset]
        if offset_string == first_string:
            return f"Первая строка получается из второй со сдвигом {offset}."
    return "Первую строку нельзя получить из второй с помощью циклического сдвига."

first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
print(find_cyclic_offset(first_string, second_string))