from collections import deque

quantity_of_food = int(input())
orders = deque([int(el) for el in input().split()])
max_order = max(orders)

while orders:
    to_remove = orders.popleft()
    if to_remove > quantity_of_food:
        orders.appendleft(to_remove)
        break
    else:
        quantity_of_food -= to_remove

print(max_order)
if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(list(map(str, orders)))}")
