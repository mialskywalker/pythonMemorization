def func(num_list):

    numbers = num_list.split()
    numbers = list(map(int, numbers))

    return f"The minimum number is {min(numbers)}\n" \
           f"The maximum number is {max(numbers)}\n" \
           f"The sum number is: {sum(numbers)}"


print(func(input()))
