def even(num_list):

    numbers = num_list.split()
    filtered = filter(lambda x: x % 2 == 0, list(map(int, numbers)))
    return list(filtered)


print(even(input()))
