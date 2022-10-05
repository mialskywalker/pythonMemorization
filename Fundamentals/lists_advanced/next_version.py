version = input().split('.')

number = int("".join(version))

number += 1

number = str(number)
number = list(map(str, number))
print(f".".join(number))
