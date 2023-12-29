# Турнир
names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
def get_participants(participants):
    return names[::2]
print("Первый день: ", get_participants(names))
