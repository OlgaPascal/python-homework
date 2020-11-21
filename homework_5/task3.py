# coding: utf-8

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("salary.txt", "r", encoding="utf-8") as fw:
    salaries = fw.readlines()

i, total = 0, 0
min = 20000
sals = dict()

for sal in salaries:
    i += 1
    name, salary = sal.split()
    total += float(salary)
    if float(salary) < min:
        print(f"{1} {name}, {salary} c окладом < {min}")
    else:
        print(f"{i} {name}, {salary}")
print(total / i)
