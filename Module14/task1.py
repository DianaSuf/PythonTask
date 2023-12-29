# Как дела?
import functools

def how_are_you(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        answer = input("Как дела? ")
        print("А у меня не очень!")
        return func(*args, **kwargs)
    return wrapper

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()