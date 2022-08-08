def factorial_div(first, second):
    first_res = 1
    second_res = 1
    first_factorial = [i for i in range(1, first + 1)]
    second_factorial = [i for i in range(1, second + 1)]

    for el in first_factorial:
        first_res *= el
    for u in second_factorial:
        second_res *= u

    return f"{(first_res / second_res):.2f}"


print(factorial_div(int(input()), int(input())))
