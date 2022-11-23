n = int(input())

matrix = []

for _ in range(n):

    matrix.append(list(map(int, input().split(', '))))

primary = [matrix[i][i] for i in range(n)]
secondary = []

for i in range(n):

    for e in range(n):

        if e + i == n-1:
            secondary.append(matrix[i][e])

print(f"Primary diagonal: {', '.join(list(map(str, primary)))}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(list(map(str, secondary)))}. Sum: {sum(secondary)}")
