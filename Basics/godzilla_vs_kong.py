import math

movie_budget = float(input())
statists_number = int(input())
clothes_price = float(input())

movie_decoration_price = movie_budget * 0.1
clothes_total = statists_number * clothes_price

if statists_number > 150:
    clothes_total -= clothes_total * 0.1

movie_total = movie_decoration_price + clothes_total
total = movie_budget - movie_total

if total >= 0:
    print(f"Action!\n"
          f"Wingard starts filming with {math.fabs(total):.2f} leva left.")
else:
    print(f"Not enough money!\n"
          f"Wingard needs {math.fabs(total):.2f} leva more.")
