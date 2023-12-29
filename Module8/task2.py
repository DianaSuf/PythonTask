# Поиск элемента — 2
def find_key(dictionary, key, depth=None):
    if depth == 0:
        return None
    if key in dictionary:
        return dictionary[key]
    else:
        for value in dictionary.values():
            if type(value) == dict:
                result = find_key(value, key, depth-1 if depth else None)
                if result is not None:
                    return result
    return None

site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}

key = input("Введите искомый ключ: ")
answer = input("Хотите ввести максимальную глубину? Y/N: ")
if answer.lower() == "y":
    depth = int(input("Введите максимальную глубину: "))
else:
    depth = None
value = find_key(site, key, depth)
print("Значение ключа:", value)