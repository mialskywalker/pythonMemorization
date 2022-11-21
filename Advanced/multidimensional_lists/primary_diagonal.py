n = int(input())

matrix = []
result = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    result += matrix[i][i]

print(result)
