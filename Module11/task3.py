# Отцы, матери и дети
class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def tell_about(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет. У меня {len(self.children)} детей.")

    def calm_child(self, child):
        print(f"{child.name}, успокойся!")
        child.calm = True

    def feed_child(self, child):
        print(f"{child.name}, покушай!")
        child.hungry = False


class Child:
    def __init__(self, name, age, calm=True, hungry=True):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry

    def tell_about(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет. Я {'спокоен' if self.calm else 'возбужден'} и {'сыт' if not self.hungry else 'голоден'}.")


parent = Parent("Иван", 40, [Child("Маша", 10), Child("Петя", 5)])
parent.tell_about()
for child in parent.children:
    child.tell_about()
    parent.calm_child(child)
    parent.feed_child(child)
    child.tell_about()