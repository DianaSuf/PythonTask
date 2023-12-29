# Видеокарты
cards_count = int(input("Количество видеокарт: "))
cards_list = []
new_list = []
max_series = 0
for i in range(cards_count):
    video_card = int(input(f"Видеокарта {i + 1}: "))
    cards_list.append(video_card)
    max_series = max(cards_list)
for video_card in cards_list:
    if video_card != max_series:
        new_list.append(video_card)
print("Старый список видеокарт: ", cards_list)
print("Новый список видеокарт: ", new_list)