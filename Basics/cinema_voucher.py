voucher = int(input())

tickets = 0
products = 0

while True:

    command = input()
    if command == "End":
        break

    if len(command) > 8:
        voucher -= ord(command[0]) + ord(command[1])
        if voucher <= 0:
            break
        tickets += 1
    else:
        voucher -= ord(command[0])
        if voucher <= 0:
            break
        products += 1

print(tickets)
print(products)
