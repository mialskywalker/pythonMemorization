n = int(input())

total = 0

for _ in range(n):

    letter = input()

    total += ord(letter)

print(f"The sum equals: {total}")
