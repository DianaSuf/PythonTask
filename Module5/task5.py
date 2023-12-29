# Пароль
while True:
    password = input('Придумайте пароль: ')
    if (len(password) >= 8 and any(char.isupper() for char in password) and sum(char.isdigit() for char in password) >= 3):
        print('Это надёжный пароль.')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        break