numbers = [int(el) for el in input().split()]
num_to_remove = int(input())

for _ in range(num_to_remove):
    to_remove = min(numbers)
    numbers.remove(to_remove)


print(", ".join(list(map(str, numbers))))
