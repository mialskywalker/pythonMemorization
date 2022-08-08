def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    sum = sum_numbers(first, second)
    total = subtract(sum, third)
    return total


print(add_and_subtract(int(input()), int(input()), int(input())))
