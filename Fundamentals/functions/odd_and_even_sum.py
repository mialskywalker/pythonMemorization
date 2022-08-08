def odd_and_even(number):

    odd = [int(el) for el in number if not int(el) % 2 == 0]
    even = [int(el) for el in number if int(el) % 2 == 0]

    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


print(odd_and_even(input()))
