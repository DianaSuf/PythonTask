# Палиндром: возвращение
can_be_palindrome = lambda s: sum([1 for i in set(s) if s.count(i) % 2 == 1]) <= 1
print(can_be_palindrome('abcba'))
print(can_be_palindrome('abbbc'))