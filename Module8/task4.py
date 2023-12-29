# Продвинутая функция sum
def sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, list):
            result += sum(*arg)
        else:
            result += arg
    return result

print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))