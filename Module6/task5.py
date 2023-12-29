# Словарь синонимов
def create_synonym_dictionary():
    pairs_count = int(input("Введите количество пар слов: "))
    dictionary = {}
    for i in range(pairs_count):
        pair = input(f"{i+1} пара слов: ").split(" — ")
        word1, word2 = pair[0].lower(), pair[1].lower()
        dictionary[word1] = word2
        dictionary[word2] = word1
    return dictionary

def find_synonym(dictionary):
    while True:
        word = input("Введите слово: ").lower()
        if word in dictionary:
            synonym = dictionary[word]
            print("Синоним: ", synonym)
            break
        else:
            print("Такого слова в словаре нет.")

synonym_dict = create_synonym_dictionary()
find_synonym(synonym_dict)