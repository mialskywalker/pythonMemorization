rows, columns = map(int, input().split())

matrix = []
temp_matrix = []
temp_result = 0
biggest_matrix = []
biggest_result = 0

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(0, rows-2):

    for e in range(0, columns-2):

        temp_matrix = []
        temp_result = matrix[i][e] + matrix[i][e+1] + matrix[i][e+2] + matrix[i+1][e] + matrix[i+1][e+1] + matrix[i+1][e+2] + matrix[i+2][e] + matrix[i+2][e+1] + matrix[i+2][e+2]
        temp_matrix.append([matrix[i][e], matrix[i][e+1], matrix[i][e+2]])
        temp_matrix.append([matrix[i+1][e], matrix[i+1][e+1], matrix[i+1][e+2]])
        temp_matrix.append([matrix[i+2][e], matrix[i+2][e+1], matrix[i+2][e+2]])
        if temp_result > biggest_result:
            biggest_result = temp_result
            biggest_matrix = temp_matrix

print(f"Sum = {biggest_result}")
for el in biggest_matrix:
    print(' '.join(map(str, el)))

