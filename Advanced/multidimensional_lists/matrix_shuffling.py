row, col = map(int, input().split())

matrix = [input().split() for _ in range(row)]

while True:

    command = input().split()

    if command[0] == 'END':
        break

    elif command[0] == 'swap' and len(command) == 5:
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])

        if row1 >= row or row2 >= row or col1 >= col or col2 >= col:
            print("Invalid input!")
        else:

            swap1 = matrix[row1][col1]
            swap2 = matrix[row2][col2]
            matrix[row2][col2] = swap1
            matrix[row1][col1] = swap2

            for r in matrix:
                print(' '.join(list(map(str, r))))

    else:
        print("Invalid input!")
