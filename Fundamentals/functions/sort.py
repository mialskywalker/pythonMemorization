def sort(num_list):

    numbers = num_list.split()
    numbers = list(map(int, numbers))

    result = sorted(numbers)

    return result


print(sort(input()))
