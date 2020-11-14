# coding: utf-8

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.


number_list = []
while True:
    items = input("Enter numbers split by space: ")
    unsafe_list = list(items)
    for a in unsafe_list:
        if a == 'q':
            print("Found special char, exiting...")
            exit()
        if a.isspace():
            continue
        try:
            a = float(a)
            number_list.append(a)
        except ValueError:
            print(f"Invalid value {a}, skiping..")
            continue
    result = sum(number_list)
    print(f"Sum is: {result:2}")


