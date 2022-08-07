amount = [int(el) for el in input().split(', ')]
beggars = int(input())

total = []
to_pay = beggars

if len(amount) == beggars:
    total = amount.copy()

elif len(amount) < beggars:
    total = amount.copy()
    while True:
        total.append(0)
        if len(total) == beggars:
            break

else:

    for i in range(beggars):

        to_add = 0
        for e in range(0, len(amount), to_pay):

            to_add += amount[e]
        amount.pop(0)
        # to_pay += 1
        total.append(to_add)

print(total)
