alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))

encrypted_message = ''
for char in message:
    if char in alphabet:
        index = (alphabet.find(char) + offset) % len(alphabet)
        encrypted_message += alphabet[index]
    else:
        encrypted_message += char

print("Зашифрованное сообщение:", encrypted_message)