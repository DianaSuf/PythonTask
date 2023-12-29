# Драка
import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, other):
        other.health -= 20
        print(f"{self.name} атаковал {other.name}. У {other.name} осталось {other.health} очков здоровья.")

    def is_alive(self):
        return self.health > 0

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.is_alive() and warrior2.is_alive():
    attacker, defender = random.sample([warrior1, warrior2], k=2)
    attacker.attack(defender)

if warrior1.is_alive():
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")