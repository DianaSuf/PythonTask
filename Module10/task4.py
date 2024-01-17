# Чат
import os

class Chat:
    def __init__(self):
        self.users = {}
        self.filename = "chat.txt"

    def add_user(self, name):
        try:
            if name in self.users:
                print(f"Пользователь {name} уже существует.")
            else:
                self.users[name] = []
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def send_message(self, name, message):
        try:
            if name not in self.users:
                print(f"Пользователь {name} не найден.")
            else:
                for user in self.users:
                    self.users[user].append((name, message))
                self.write_chat_to_file()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def view_chat(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def write_chat_to_file(self):
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                for user in self.users:
                    for message in self.users[user]:
                        f.write(f"{message[0]}: {message[1]}\n")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")


chat = Chat()

while True:
    try:
        print("1. Добавить пользователя")
        print("2. Отправить сообщение")
        print("3. Посмотреть чат")
        action = input("Выберите действие: ")

        if action == "1":
            name = input("Введите имя пользователя: ")
            chat.add_user(name)
        elif action == "2":
            name = input("Введите ваше имя: ")
            message = input("Введите сообщение: ")
            chat.send_message(name, message)
        elif action == "3":
            chat.view_chat()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
