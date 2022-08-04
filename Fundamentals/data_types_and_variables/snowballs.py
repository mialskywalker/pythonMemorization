number_of_snowballs = int(input())

highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for _ in range(number_of_snowballs):

    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    current_value = (weight / time_needed) ** quality

    if current_value > highest_value:
        highest_value = current_value
        highest_weight = weight
        highest_time = time_needed
        highest_quality = quality

print(f"{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})")
