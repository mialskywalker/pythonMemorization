import math

budget = float(input())
sleepover_number = int(input())
sleepover_price = float(input())
extras_price = int(input())

total = 0
extras = 0
discount = 0
sleep = 0

if sleepover_number > 7:
    extras = budget * (0.01 * extras_price)
    discount = sleepover_price * 0.05
    sleep = sleepover_number * (sleepover_price - discount)
    total = extras + sleep

else:
    extras = budget * (0.01 * extras_price)
    sleep = sleepover_number * sleepover_price
    total = extras + sleep


if total > budget:
    print(f"{math.fabs(total - budget):.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {(budget - total):.2f} leva after vacation.")
