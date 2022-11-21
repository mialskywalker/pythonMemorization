n = int(input())

matrix = []

for rows in range(n):

    matrix.append([int(el) for el in input().split(', ') if int(el) % 2 == 0])

print(matrix)
