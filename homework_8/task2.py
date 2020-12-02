# coding: utf-8
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class DivisionByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        n = int(input("Enter number: "))
        if n == 0:
            raise DivisionByZeroException("Division by zero error, please enter value != 0")
        print(f"Result: {100 / n}")
    except DivisionByZeroException as e:
        print(f"Вы ввели 0. Сработало исключение \n {e}")
    except ValueError:
        print("Только числа!")