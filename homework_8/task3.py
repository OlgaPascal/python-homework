 # 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
class NotANumberError(ValueError):
    pass


class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


n = []
while True:
    inp = input("Enter number: ")
    if 'stop' in inp:
        break

    # Solution 1
    try:
        if not inp.isnumeric():
            raise OnlyNumber("Only numeric accepted")
        else:
            n.append(inp)
    except OnlyNumber as e:
        print(f"Сработало исключение {e}")

    # comment solution 1 and uncomment code below
    # n.append(inp)

# solution 2 check the whole list
# try:
#     if any(map(lambda x: not x.isnumeric(), n)):
#         raise OnlyNumber("Only numeric accepted")
# except OnlyNumber as e:
#     print(e)
# else:
#     print(n)

print(n)