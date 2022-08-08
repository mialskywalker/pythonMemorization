def smallest_number(first, second, third):
    if first <= second and first <= third:
        print(first)
    elif second <= first and second <= third:
        print(second)
    elif third <= first and third <= second:
        print(third)


smallest_number(int(input()), int(input()), int(input()))
