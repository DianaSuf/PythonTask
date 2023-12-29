# Анализ комментариев
def count_uppercase_lowercase(text):
    upper = len([char for char in text if char.isupper()])
    lower = len([char for char in text if char.islower()])
    return upper, lower

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)