rows, columns = map(int, input().split(', '))

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(columns):
    result = 0
    for e in range(rows):
        result += matrix[e][i]
    print(result)
