# Случайные соревнования
import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_team[index], second_team[index]) for index in range(20)]
print("Первая команда: ", first_team)
print(f"Вторая команда: ", second_team)
print(f"Победители тура: ", winners)