rows, columns = map(int, input().split(', '))

matrix = []
temp_matrix = []
temp_result = 0
biggest_matrix = []
biggest_result = 0

for _ in range(rows):
    matrix.append(list(map(int, input().split(', '))))

for i in range(0, rows-1):

    for e in range(0, columns-1):

        temp_matrix = []
        temp_result = matrix[i][e] + matrix[i][e+1] + matrix[i+1][e] + matrix[i+1][e+1]
        temp_matrix.append([matrix[i][e], matrix[i][e+1]])
        temp_matrix.append([matrix[i+1][e], matrix[i+1][e+1]])
        if temp_result > biggest_result:
            biggest_result = temp_result
            biggest_matrix = temp_matrix

for el in biggest_matrix:
    print(' '.join(map(str, el)))
print(biggest_result)
