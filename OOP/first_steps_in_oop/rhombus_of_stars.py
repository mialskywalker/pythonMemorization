def down(num):
    for i in range(num - 2, -1, -1):
        print(rhombus(i))


def up(num):
    for i in range(num):
        print(rhombus(i))


def rhombus(i):
    offset = (n - i - 1) * ' '
    content = ('* ' * (i+1)).strip()
    return f"{offset}{content}"


n = int(input())

up(n)
down(n)
