import math

n = int(input())

matrix = []

for _ in range(n):

    matrix.append(list(map(int, input().split())))

primary = [matrix[i][i] for i in range(n)]
secondary = []

for i in range(n):

    for e in range(n):

        if e + i == n-1:
            secondary.append(matrix[i][e])

print(f"{(math.fabs(sum(primary)-sum(secondary))):.0f}")
