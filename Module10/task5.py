# Надёжные вычисления
import math

def sqrt_with_exception_handling(number):
    try:
        if number < 0:
            raise ValueError("Число не может быть отрицательным")
        result = math.sqrt(number)
        return result
    except Exception as exc:
        print(f"Произошла ошибка: {exc}")

print(sqrt_with_exception_handling(9))
print(sqrt_with_exception_handling(-1))
