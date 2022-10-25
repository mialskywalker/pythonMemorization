clothes = list(map(int, input().split()))
rack_size = int(input())

num_of_racks = 1
current_rack = rack_size

while clothes:

    first = clothes.pop()
    if current_rack < first:
        num_of_racks += 1
        clothes.append(first)
        current_rack = rack_size
    elif current_rack > first:
        current_rack -= first
    elif current_rack == first:
        num_of_racks += 1
        current_rack = rack_size

print(num_of_racks)
