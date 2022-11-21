rows, columns = input().split(', ')
matrix = []

for i in range(int(rows)):
    matrix.append([int(el) for el in input().split(', ')])

print(sum(map(sum, matrix)))
print(matrix)
