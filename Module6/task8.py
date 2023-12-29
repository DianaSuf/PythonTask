# Снова палиндром
def can_make_palindrome(s):
    char_count, odd_count = dict(), 0
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1

print("Можно сделать палиндромом") if can_make_palindrome(input("Введите строку: ")) else print("Нельзя сделать палиндромом")