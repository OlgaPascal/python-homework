# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
# products = [
#     (1, {"name": "computer", "price": 20000, "quantity": 5, "u": "items"}),
#     (1, {"name": "printer", "price": 6000, "quantity": 2, "u": "items"}),
#     (1, {"name": "scanner", "price": 2000, "quantity": 7, "u": "items"})
# ]
products = []

for i in range(3):
    index = len(products) + 1
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    unit = input("Enter product unit: ")
    product = {"name": name, "price": price, "quantity":quantity, "unit": unit}
    products.append((index, product))

print(products)

# products = [(1, {'name': 'computer', 'price': '2000', 'quantity': '4', 'unit': 'piece'}), (2, {'name': 'scanner', 'price': '2000', 'quantity': '5', 'unit': 'piece'}), (3, {'name': 'printer', 'price': '4000', 'quantity': '3', 'unit': 'piece'})]

stats = {"name": set(), "price": set(), "quantity": set(), "unit": set() }
for idx, product in products:
    stats["name"].add(product["name"])
    stats["price"].add(product["price"])
    stats["quantity"].add(product["quantity"])
    stats["unit"].add(product["unit"])
print(stats)