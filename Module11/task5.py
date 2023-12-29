# Совместное проживание
from random import randint, choice

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        if self.house.food > 0:
            self.satiety += 1
            self.house.food -= 1
            return f"{self.name} ест, сытость {self.satiety}, еда {self.house.food}"
        else:
            return f"{self.name} не может поесть, в доме нет еды"

    def work(self):
        if self.satiety > 0:
            self.satiety -= 1
            self.house.money += 1
            return f"{self.name} работает, сытость {self.satiety}, деньги {self.house.money}"
        else:
            return f"{self.name} не может работать, он умер с голоду"

    def play(self):
        if self.satiety > 0:
            self.satiety -= 1
            return f"{self.name} играет, сытость {self.satiety}"
        else:
            return f"{self.name} не может играть, он умер с голоду"

    def repast(self):
        if self.house.money > 0:
            self.house.food += 1
            self.house.money -= 1
            return f"{self.name} идет в магазин, еда {self.house.food}, деньги {self.house.money}"
        else:
            return f"{self.name} не может пойти в магазин, в доме нет денег"

    def live_one_day(self):
        number_cubes = randint(1, 6)
        if self.satiety < 0:
            return f"{self.name} умер с голоду"
        elif self.satiety < 20:
            return self.eat()
        elif self.house.food < 10:
            return self.repast()
        elif self.house.money < 50:
            return self.work()
        elif number_cubes == 1:
            return self.work()
        elif number_cubes == 2:
            return self.eat()
        else:
            return self.play()

house = House()
person_1 = Person("Вася", house)
person_2 = Person("Федя", house)

for i in range(365):
    person = choice([person_1, person_2])
    print(person.live_one_day())

print("Все плохо" if person.satiety < 0 else "Выжили")