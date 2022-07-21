drink_type = input()
sugar = input()
drinks_number = int(input())

coffee_price = 0
discount = 0
discount_espresso = 0

if drink_type == "Espresso":
    if drinks_number > 5:
        discount_espresso = 0.25
    if sugar == "Without":
        coffee_price = 0.9
        discount = 0.35
    elif sugar == "Normal":
        coffee_price = 1
    elif sugar == "Extra":
        coffee_price = 1.20

elif drink_type == "Cappuccino":
    if sugar == "Without":
        coffee_price = 1
        discount = 0.35
    elif sugar == "Normal":
        coffee_price = 1.20
    elif sugar == "Extra":
        coffee_price = 1.60

elif drink_type == "Tea":
    if sugar == "Without":
        coffee_price = 0.50
        discount = 0.35
    elif sugar == "Normal":
        coffee_price = 0.60
    elif sugar == "Extra":
        coffee_price = 0.70

drinks_price = drinks_number * coffee_price
first_price = drinks_price - (drinks_price * discount)
total_price = first_price - (first_price * discount_espresso)

if total_price > 15:
    total_price = total_price - (total_price * 0.2)

print(f"You bought {drinks_number} cups of {drink_type} for {total_price:.2f} lv.")