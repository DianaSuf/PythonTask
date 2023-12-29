# Весь мир — декоратор…
from typing import Callable

def decorator_with_args_for_any_decorator(decorator: Callable[..., Callable]) -> Callable[..., Callable]:
    def decorated_decorator(*args, **kwargs) -> Callable[..., Callable]:
        def wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return wrapper
    return decorated_decorator

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)