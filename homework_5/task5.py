# coding: utf-8

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("task5.txt", "r+", encoding="utf-8") as fw:
    fw.write(" ".join(map(str, list(range(1, 100)))))
    fw.seek(0)
    print(sum(map(int, fw.read().split())))
