# Пицца
orders = dict()
orders_count = int(input("Введите количество заказов: "))

for i in range(orders_count):
    order = input(f"{i + 1} заказ: ").split()
    customer, pizza, quantity = order[0], order[1], int(order[2])

    if customer not in orders:
        orders[customer] = {}
    orders[customer][pizza] = orders[customer].get(pizza, 0) + quantity

for customer in orders.keys():
    print(customer + ":")
    for pizza, quantity in orders[customer].items():
        print(pizza + ": " + str(quantity))