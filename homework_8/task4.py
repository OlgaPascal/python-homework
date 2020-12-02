# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.
# print(stock.show())
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.
##

class Equipment:
    """
    owner - is the name of division who owns equipment
    """
    name = str
    make = str
    year = str
    owner = str

    def __init__(self, serial, make, year):
        self.serial = serial
        self.make = make
        self.year = year
        self.owner = None

    def __str__(self):
        return f"{self.__class__.__name__}\nSerial number: {self.serial}\nmake: {self.make}\nowner: {self.owner}\n"


class NotAnEquipment(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    items = []
    total = 0

    def show(self):
        print(f"Total in stock {self.total} items")
        for i in self.items:
            print(i)
            print(100*'-')

    def add(self, item):
        self.total += 1
        if not isinstance(item, Equipment):
            raise NotAnEquipment('Can not add equipment. Must be Equipment object')
        else:
            self.items.append(item)

    def remove(self, item):
        for k, i in enumerate(self.items):
            if i.serial == item.serial:
                del self.items[k]
                self.total -= 1
                break

    def move(self, item, owner):
        found = item in self.items
        if found:
            self.remove(item)
            item.owner = owner
            owner.add_equipment(item)
            print(f"Move ownership to {owner}")


class Department():
    equipment = list()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} department"

    def add_equipment(self, obj):
        self.equipment.append(obj)


class Company:
    name = 'Apple'
    deps = []

    def __str__(self):
        return f"Company: {self.name}"

    def add(self, department):
        if not isinstance(department, Department):
            raise Exception('Can not add department. Must be a Department object')
        else:
            self.deps.append(department)

    def department(self, name):
        for d in self.deps:
            if d.name == name:
                return d

    def show_deps(self):
        for i in self.deps:
            print(i)



class Printer(Equipment):
    pass


class Scanner(Equipment):
    lamp_power = None

    def __init__(self, *args, **kwargs):
        self.lamp_power = kwargs.pop('lamp_power')
        super(Scanner, self).__init__(*args, **kwargs)

    def get_lamp_power(self):
        return self.lamp_power


class Xerox(Equipment):
    def __init__(self, *args, **kwargs):
        super(Xerox, self).__init__(*args, **kwargs)


stock = Stock()
printer1 = Printer(serial='3403408039840', make="Epson", year='2019')
stock.add(printer1)
stock.add(Scanner(serial='9103308039840', make="HP", year="2016", lamp_power=200))
stock.add(Xerox(serial='8107308039840', make="Canon", year='2010'))

company = Company()
company.add(Department(name='IT'))
company.add(Department(name='Marketing'))

print(company)

print(stock.show())
it = company.department('IT')
stock.move(printer1, it)

print(f"Owner of {printer1} now is {printer1.owner}")
print(it.equipment)
print(stock.show())


print("\n"*3)
# now let's get an exception
try:
    stock.add("WrongItem")
except NotAnEquipment as e:
    print(e)

try:
    company.add("SomethingInvalid")
except Exception as e:
    print(e)


#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.
