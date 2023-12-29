# Замедление кода
import time
import functools

def wait(seconds: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@wait(seconds=3)
def some_function():
    print("Сделано!")


print("Выполним какую-то функцию...")
some_function()