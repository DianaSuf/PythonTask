# Глубокое копирование
import copy

def find_and_replace(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
    else:
        for k, v in dictionary.items():
            if isinstance(v, dict):
                find_and_replace(v, key, value)

def create_sites():
    site = {
    'html': {
    'head': {
    'title': 'Куплю/продам телефон недорого'
    },
    'body': {
    'h2': 'У нас самая низкая цена на iPhone',
    'div': 'Купить',
    'p': 'Продать'
    }
    }
    }

    sites = []
    n = int(input('Сколько сайтов: '))
    for i in range(n):
        product = input('Введите название продукта для нового сайта: ')
        new_site = copy.deepcopy(site)
        find_and_replace(new_site, 'title', f'Куплю/продам {product} недорого')
        find_and_replace(new_site, 'h2', f'У нас самая низкая цена на {product}')
        sites.append(new_site)
        for j, site in enumerate(sites, 1):
            print(f'Сайт для {site["html"]["head"]["title"][10:-9]}:')
            print(f'site = {site}')

create_sites()