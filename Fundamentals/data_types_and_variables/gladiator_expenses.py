lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_count = 0
sword_count = 0
shield_count = 0
armor_count = 0

for i in range(1, lost_fights+1):

    if i % 2 == 0 and i % 3 == 0:
        shield_count += 1
        if shield_count % 2 == 0:
            armor_count += 1
    if i % 2 == 0:
        helmet_count += 1
    if i % 3 == 0:
        sword_count += 1

total = (helmet_price * helmet_count) + (sword_price * sword_count) \
        + (shield_price * shield_count) + (armor_price * armor_count)

print(f"Gladiator expenses: {total:.2f} aureus")
