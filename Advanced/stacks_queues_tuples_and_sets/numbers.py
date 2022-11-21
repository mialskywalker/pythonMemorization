first_sequence = set(int(el) for el in input().split())
second_sequence = set(int(el) for el in input().split())

n = int(input())

for i in range(n):

    sequence = set()
    command = input().split()

    if command[0] == 'Add':
        if command[1] == 'First':
            for e in range(2, len(command)):
                sequence.add(int(command[e]))
            first_sequence = first_sequence.union(sequence)
        elif command[1] == 'Second':
            for e in range(2, len(command)):
                sequence.add(int(command[e]))
            second_sequence = second_sequence.union(sequence)

    elif command[0] == 'Remove':
        if command[1] == 'First':
            for e in range(2, len(command)):
                if int(command[e]) in first_sequence:
                    first_sequence.remove(int(command[e]))
        elif command[1] == 'Second':
            for e in range(2, len(command)):
                if int(command[e]) in second_sequence:
                    second_sequence.remove(int(command[e]))

    elif command[0] == 'Check' and command[1] == 'Subset':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print('False')

print(', '.join(map(str, first_sequence)))
print(', '.join(map(str, second_sequence)))
