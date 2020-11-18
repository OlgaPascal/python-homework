# coding: utf-8
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
err_msg = "Missing required arguments or invalid type! Please enter: hours, price_per_hour, bonus as numbers"

def salary(hours, price_per_hour, bonus):
    print(hours, price_per_hour, bonus)
    hours, price_per_hour, bonus = int(hours), int(price_per_hour), int(bonus)
    if not hours or not price_per_hour or not bonus:
        print(err_msg)
    return hours * price_per_hour + bonus

if len(argv) < 4:
    exit(err_msg)
if not all(x.isnumeric() for x in argv[1:]):
    # err_msg = [x.isnumeric() for x in argv[1:]]
    exit(err_msg)
print(salary(hours=argv[1], price_per_hour=argv[2], bonus=argv[3]))

