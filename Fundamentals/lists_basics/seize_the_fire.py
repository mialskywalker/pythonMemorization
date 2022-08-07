HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

text = input().split('#')
amount_of_water = int(input())

total_fire_put_out = 0
total_effort = 0
current_effort = 0
current_water = amount_of_water
cells = []

for el in text:

    fire_type, value = el.split(' = ')
    value = int(value)

    if fire_type == 'High':
        if value in HIGH:
            if current_water >= value:
                current_water -= value
                current_effort = value * 0.25
                total_effort += current_effort
                total_fire_put_out += value
                cells.append(value)
    elif fire_type == 'Medium':
        if value in MEDIUM:
            if current_water >= value:
                current_water -= value
                current_effort = value * 0.25
                total_effort += current_effort
                total_fire_put_out += value
                cells.append(value)
    elif fire_type == 'Low':
        if value in LOW:
            if current_water >= value:
                current_water -= value
                current_effort = value * 0.25
                total_effort += current_effort
                total_fire_put_out += value
                cells.append(value)

print('Cells:')
for cell in cells:
    print(f'- {cell}')
print(f"Effort: {total_effort:.2f}\n"
      f"Total Fire: {total_fire_put_out}")
