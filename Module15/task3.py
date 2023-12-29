# Дата
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        day, month, year = map(int, date_string.split('-'))
        if cls.is_date_valid(day, month, year):
            return cls(day, month, year)
        else:
            raise ValueError('Invalid date!')

    @staticmethod
    def is_date_valid(day: int, month: int, year: int) -> bool:
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True

    def __str__(self):
        return f'День: {self.__day}\tМесяц: {self.__month}\tГод: {self.__year}'

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid(10, 12, 2077))
print(Date.is_date_valid(40, 12, 2077))