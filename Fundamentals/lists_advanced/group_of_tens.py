numbers = list(map(int, input().split(', ')))
min = 1
max = 11
iter = 0
while numbers:
    group = []
    for el in numbers:
        if el in range(min, max):
            group.append(el)
    if len(group) > 0:
        for el in group:
            numbers.remove(el)
    iter += 1
    print(f"Group of {iter*10}'s: {group}")

    min += 10
    max += 10
