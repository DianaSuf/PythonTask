# Счётчик
import functools
import random

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.count} раз")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@counter
def first_func() -> None:
    print("Вызвана 1-ая функция!")

@counter
def second_func() -> None:
    print("Вызвана 2-ая фукция!")


for func in [first_func, second_func]:
    for _ in range(random.randint(1, 20)):
        func()

print(CALLS)