# Гистограмма частоты — 2
def get_character_frequencies(text):
    frequency_dict = {}
    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict


def invert_frequency_dict(frequency_dict):
    inverted_dict = {}
    for char, frequency in frequency_dict.items():
        if frequency in inverted_dict:
            inverted_dict[frequency].append(char)
        else:
            inverted_dict[frequency] = [char]

    return inverted_dict


text = input("Введите текст: ")
frequency_dict = get_character_frequencies(text)
inverted_dict = invert_frequency_dict(frequency_dict)

print("Оригинальный словарь частот:")
for char, frequency in frequency_dict.items():
    print(char, ":", frequency)
print("Инвертированный словарь частот:")
for frequency, chars in inverted_dict.items():
    print(frequency, ":", chars)