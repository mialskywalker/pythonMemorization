groceries = {}

while True:

    command = input()

    if command == 'buy':
        break

    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in groceries.keys():

        groceries[product] = [quantity, price]

    else:

        for k, v in groceries.items():
            if k == product:
                v[0] += quantity
                v[1] = price


for k, v in groceries.items():
    result = v[0] * v[1]
    print(f"{k} -> {result:.2f}")
