rows, columns = map(int, input().split())

matrix = [input().split() for _ in range(rows)]
identical = 0

for r in range(rows-1):
    for c in range(columns-1):

        if matrix[r][c] == matrix[r+1][c+1] == matrix[r][c+1] == matrix[r+1][c]:
            identical += 1

print(identical)
