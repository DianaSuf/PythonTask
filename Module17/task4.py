# Уникальный шифр
from collections import Counter

def count_unique_char(string: str) -> int:
    return sum(1 for i in Counter(string).values() if i == 1)

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_char(message)
print("Количество уникальных символов в строке:", unique_count)