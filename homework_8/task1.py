# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def fetch(cls, date):
        day, month, year = date.split('-')
        print(day, month, year)
        return f"{day}{month}"

    @staticmethod
    def validate_date(date):
        day, month, year = date.split('-')
        assert 0 < int(day) < 31
        assert 0 < int(month) < 13
        assert 0 < int(year) < 2020
        return True


c = Date("20-04-2019")
print(Date.fetch(c.date))
print(Date.validate_date(c.date))
print(Date.validate_date("700-3343-34343"))

