# Кэширование для ускорения вычислений
import functools
from typing import Dict, Callable, Any

HASH: Dict[Callable, Dict[Any, Any]] = dict()

@functools.cache
def fibonacci(n: int) -> int:
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1

print(fibonacci(52))