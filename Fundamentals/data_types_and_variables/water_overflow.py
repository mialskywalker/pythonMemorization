n = int(input())

capacity = 255
liters_in_tank = 0

for _ in range(n):

    liters = int(input())

    if capacity - liters < 0:
        print("Insufficient capacity!")
    else:
        capacity -= liters
        liters_in_tank += liters

print(liters_in_tank)
