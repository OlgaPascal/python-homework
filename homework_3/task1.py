# coding: utf-8
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(x, y):
    try:
        return round(x / y, 2)
    except ZeroDivisionError:
        print("Division by zero, try enter again")
        return

while True:
    numbers = []
    print("Enter two numbers")
    while len(numbers) < 2:
        try:
            v = float(input("Enter number: "))
            numbers.append(v)
        except ValueError:
            print("Invalid value type, try enter again")
            continue
        # found in internet
        except KeyboardInterrupt:
            exit('Stopped')
    result = division(numbers[0], numbers[1])
    if not result:
        continue
    print(f"Result is: {result:2}")



