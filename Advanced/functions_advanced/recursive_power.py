from functools import reduce


def recursive_power(number, power):

    return reduce(lambda x, y: x**y, [number, power])


print(recursive_power(2, 10))
print(recursive_power(10, 100))
