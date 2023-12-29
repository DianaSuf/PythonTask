# Анализ слова — 2
str = str(input("Введите слово: "))
palindrome = str[::-1]
if str == palindrome:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")