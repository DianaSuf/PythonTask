# Контакты — 3
contacts = {}
def add_contact():
    name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
    if (name, surname) in contacts:
        print("Такой человек уже есть в контактах.")
    else:
        phone = input("Введите номер телефона: ")
        contacts[(name, surname)] = phone
    print("Текущий словарь контактов:", contacts)

def find_contact():
    surname = input("Введите фамилию для поиска: ")
    surname = surname.lower()
    found = []
    for (name, sname), phone in contacts.items():
        sname = sname.lower()
        if sname == surname:
            found.append((name, sname, phone))
    if found:
        print("Найденные контакты:")
        for name, sname, phone in found:
            print(name, sname, phone)
    else:
        print("Нет контактов с такой фамилией.")

while True:
    print("Введите номер действия:")
    print("1. Добавить контакт.")
    print("2. Найти человека.")
    action = input()
    if action == "1":
        add_contact()
    elif action == "2":
        find_contact()
    else:
        print("Неверный номер действия.")