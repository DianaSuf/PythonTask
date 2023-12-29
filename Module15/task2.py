# Математический модуль
from math import pi

class MyMath:
    @staticmethod
    def circle_len(radius: float) -> float:
        """Вычисляет длину окружности по радиусу"""
        return 2 * pi * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        """Вычисляет площадь окружности по радиусу"""
        return pi * radius ** 2

    @staticmethod
    def cube_vol(side: float) -> float:
        """Вычисляет объём куба по длине ребра"""
        return side ** 3

    @staticmethod
    def sphere_sq(radius: float) -> float:
        """Вычисляет площадь поверхности сферы по радиусу"""
        return 4 * pi * radius ** 2

math = MyMath()
res_1 = math.circle_len(radius=5)
res_2 = math.circle_sq(radius=6)
print(res_1)
print(res_2)