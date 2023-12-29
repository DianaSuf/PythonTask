# Контейнеры
num_containers = int(input("Количество контейнеров: "))

if num_containers <= 0 or num_containers > 200:
    print("Некорректное количество контейнеров. Пожалуйста, введите число от 1 до 200.")
else:
    container_weights = []
    for i in range(num_containers):
        weight = int(input("Введите вес контейнера: "))
        if weight <= 0 or weight > 200:
            print("Некорректный вес контейнера. Пожалуйста, введите число от 1 до 200.")
            break
        container_weights.append(weight)
    else:
        new_container_weight = int(input("Введите вес нового контейнера: "))
        if new_container_weight <= 0 or new_container_weight > 200:
            print("Некорректный вес нового контейнера. Пожалуйста, введите число от 1 до 200.")
        else:
            position = 1
            for weight in container_weights:
                if new_container_weight < weight:
                    position += 1
                else:
                    break
            print(f"Номер, который получит новый контейнер: {position}")