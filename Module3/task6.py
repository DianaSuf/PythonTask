# Ролики
num_of_skates = int(input("Количество роликов: "))
roller_sizes = []
for i in range(num_of_skates):
    size = int(input(f"Размер ролика {i + 1}: "))
    roller_sizes.append(size)

num_of_people = int(input("Количество людей: "))
foot_sizes = []
for i in range(num_of_people):
    size = int(input(f"Размер ноги человека {i + 1}: "))
    foot_sizes.append(size)

roller_sizes.sort()
foot_sizes.sort()

count = 0
foot_index = 0
for roller_size in roller_sizes:
    if foot_index >= num_of_people:
        break
    while foot_index < num_of_people and foot_sizes[foot_index] < roller_size:
        foot_index += 1
    if foot_index < num_of_people and foot_sizes[foot_index] == roller_size:
        count += 1
        foot_index += 1

print("Наибольшее количество людей, которые могут взять ролики:", count)