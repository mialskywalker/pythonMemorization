n = int(input())

matrix = []

for _ in range(n):
    row = list(map(int, input().split(', ')))
    for i in range(len(row)):
        matrix.append(row[i])

print(matrix)
