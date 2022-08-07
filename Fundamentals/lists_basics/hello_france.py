text = input().split('|')
budget = float(input())
bought_items = []
profit = 0
new_prices = []

old_budget = budget
new_budget = 0

for el in text:

    product, price = el.split('->')
    price = float(price)

    if product == 'Clothes':
        if 0 < price <= 50.00:
            if old_budget >= price:
                bought_items.append(price)
                old_budget -= price
    elif product == 'Shoes':
        if 0 < price <= 35.00:
            if old_budget >= price:
                bought_items.append(price)
                old_budget -= price
    elif product == 'Accessories':
        if 0 < price <= 20.50:
            if old_budget >= price:
                bought_items.append(price)
                old_budget -= price

for prices in bought_items:
    profit += prices * 0.4
    value = f"{prices + (prices * 0.4):.2f}"
    new_prices.append(value)

new_budget = old_budget + sum(list(map(float, new_prices)))

print(' '.join(list(map(str, new_prices))))
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
