films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
favorite_films_count = int(input('Сколько фильмов хотите добавить? '))

for i in range(favorite_films_count):
    film = input('Введите название фильма: ')
    if film in films:
        favorite_films.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print('Ваш список любимых фильмов:', ', '.join(favorite_films))