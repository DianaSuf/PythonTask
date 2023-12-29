# Квадраты чисел
class SquaresIterator:
    def __init__(self, n: int):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

def squares_generator(n: int):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


squares = (i ** 2 for i in range(1, n + 1))