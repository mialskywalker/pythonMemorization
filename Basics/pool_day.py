import math

number_of_people = int(input())
ticket_price = float(input())
lounger_price = float(input())
umbrella_price = float(input())

total_ticket = number_of_people * ticket_price
loungers = math.ceil(number_of_people * 0.75) * lounger_price
umbrellas = math.ceil(number_of_people * 0.5) * umbrella_price

total = total_ticket + loungers + umbrellas

print(f"{total:.2f} lv.")
