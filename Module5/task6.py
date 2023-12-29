# Сжатие
string = input("Введите строку: ")
def encode_string(string):
    encoded_string = ""
    count = 1
    for i in range(len(string)):
        if i == len(string) - 1 or string[i] != string[i+1]:
            encoded_string += string[i] + str(count)
            count = 1
        else:
            count += 1
    return encoded_string

encoded_string = encode_string(string)
print("Закодированная строка:", encoded_string)