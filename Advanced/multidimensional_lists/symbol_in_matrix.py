n = int(input())

matrix = []
symbol_row = 0
symbol_column = 0
has_symbol = False

for _ in range(n):
    matrix.append([el for el in input()])

symbol = input()

for row in range(len(matrix)):
    for column in range(len(matrix[row])):

        if matrix[row][column] == symbol:
            has_symbol = True
            symbol_row = row
            symbol_column = column
            break
    if has_symbol:
        break

if has_symbol:
    print(f"({symbol_row}, {symbol_column})")
else:
    print(f"{symbol} does not occur in the matrix")
