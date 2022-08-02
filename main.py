num_of_orders = int(input())
total = 0
total_for_order = 0

for _ in range(num_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if 0.01 <= price <= 100.00:
        if 1 <= days <= 31:
            if 1 <= capsules <= 2000:
                total_for_order = price * capsules * days

    if total_for_order > 0:
        print(f"The price for the coffee is: ${total_for_order:.2f}")
        total += total_for_order


print(f"Total: ${total:.2f}")
