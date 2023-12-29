# Вечеринка
guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: ", guests)
    guest_action = input("Гость пришёл или ушёл? ")
    if (guest_action == "Пора спать"):
        print("Вечеринка закончилась, все легли спать.")
        break
    else:
        guest_name = input("Имя гостя: ")
        if guest_action == "пришёл":
            if (len(guests) != 6):
                print(f"Привет, {guest_name}!")
                guests.append(guest_name)
            else:
                print(f"Прости, {guest_name}, но мест нет.")
        elif (guest_action == "ушёл"):
            if guest_name in guests:
                print(f"Пока, {guest_name}!")
                guests.remove(guest_name)
            else:
                print("Ошибка")
    print()