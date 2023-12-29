# Заглавные буквы
str = input("Введите строку: ").split()
for i in range(len(str)):
    str[i] = str[i][0].upper() + str[i][1:]
print(' '.join(str))