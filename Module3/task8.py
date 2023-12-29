# Симметричная последовательность
num_of_numbers = int(input("Количество чисел: "))
sequence = [int(input("Число: ")) for i in range(num_of_numbers)]

def is_symmetric(sequence):
    return sequence == sequence[::-1]

to_add = []
i = 0
while i < len(sequence) and not is_symmetric(sequence + to_add):
    to_add.insert(0, sequence[i])
    i += 1

print("Последовательность: ", sequence)
print("Нужно приписать чисел: ", len(to_add))
print("Сами числа: ", to_add)