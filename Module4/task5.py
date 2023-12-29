# Разворот
str = input("Введите строку: ")
first_h = str.index('h')
last_h = str.rindex('h')
reversed = str[first_h + 1:last_h][::-1]
print("Развёрнутая последовательность между первым и последним h:", reversed)