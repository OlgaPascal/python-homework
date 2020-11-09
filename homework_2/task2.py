# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

mylist_str = input("enter number separated by comma")
mylist = mylist_str.split(",")

# mylist = [0, 1, 3, 2, 4, 5, 7, 9, 10]
new = []
last = len(mylist)
for el in range(len(mylist)):
    if el % 2 != 0:
        continue
    curr = mylist.pop(el)
    mylist.insert(el+1, curr)
print(mylist)