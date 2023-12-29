# Три списка
def find_common_elements(array_1, array_2, array_3):
    # Задача 1 без использования множеств
    common_elements_1 = []
    for element in array_1:
        if element in array_2 and element in array_3:
            common_elements_1.append(element)

    # Задача 1 с использованием множеств
    set_1, set_2, set_3 = set(array_1), set(array_2), set(array_3)
    common_elements_2 = list(set_1.intersection(set_2, set_3))
    return common_elements_1, common_elements_2

def find_unique_elements(array_1, array_2, array_3):
    # Задача 2 без использования множеств
    unique_elements_1 = []
    for element in array_1:
        if element not in array_2 and element not in array_3:
            unique_elements_1.append(element)

    # Задача 2 с использованием множеств
    set_1, set_2, set_3 = set(array_1), set(array_2), set(array_3)
    unique_elements_2 = list(set_1.difference(set_2.union(set_3)))
    return unique_elements_1, unique_elements_2


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_elements_solution_1, common_elements_solution_2 = find_common_elements(array_1, array_2, array_3)
unique_elements_solution_1, unique_elements_solution_2 = find_unique_elements(array_1, array_2, array_3)

print("Задача 1:")
print("Решение без множеств:", common_elements_solution_1)
print("Решение с множествами:", common_elements_solution_2)

print("Задача 2:")
print("Решение без множеств:", unique_elements_solution_1)
print("Решение с множествами:", unique_elements_solution_2)