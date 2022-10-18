stack = []

n = int(input())

for _ in range(n):

    command = input().split()

    if command[0] == '1':
        num = int(command[1])
        stack.append(num)
    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
    elif command[0] == '3':
        print(max(stack))
    elif command[0] == '4':
        print(min(stack))

print(', '.join(reversed(list(map(str, stack)))))
