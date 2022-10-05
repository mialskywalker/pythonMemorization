electrons_number = int(input())

electrons = electrons_number
shells = []
result = 0
iteration = 0

while electrons > 0:

    iteration += 1
    result = 2 * (iteration**2)
    if electrons >= result:
        shells.append(result)
        electrons -= result
    else:
        shells.append(electrons)
        electrons = 0

print(shells)
