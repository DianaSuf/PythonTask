# Песни — 2
violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
songs_count = int(input("Сколько песен выбрать? "))
time = 0
current_song = 1

for i in range(songs_count):
    song_name = input(f'Название {current_song} песни: ')
    if song_name in violator_songs:
        time += violator_songs[song_name]
        current_song += 1

print("Общее время звучания песен: {:.2f} минут".format(time))