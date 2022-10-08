n = int(input())
parking_lot = {}


for _ in range(n):

    text = input().split()

    if len(text) == 3:
        command, name, number = text
        if name in parking_lot.keys():
            print(f"ERROR: already registered with plate number {parking_lot[name]}")
        else:
            parking_lot[name] = number
            print(f"{name} registered {parking_lot[name]} successfully")

    elif len(text) == 2:
        command, name = text
        if name not in parking_lot.keys():
            print(f"ERROR: user {name} not found")
        else:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")

for k, v in parking_lot.items():
    print(f"{k} => {v}")
