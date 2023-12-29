# Самое длинное слово
str = input("Введите строку: ").split()
longest_str = max(str, key=len)
print(f"Самое длинное слово: «{longest_str}».")
print(f"Длина этого слова: {len(longest_str)}.")