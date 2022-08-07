name_of_gifts = input().split()

command = input()

while command != 'No Money':

    command = command.split()

    if command[0] == 'OutOfStock':
        for i in range(len(name_of_gifts)):
            if name_of_gifts[i] == command[1]:
                name_of_gifts.pop(i)
                name_of_gifts.insert(i, 'None')
    elif command[0] == 'Required':
        if int(command[2]) < len(name_of_gifts):
            name_of_gifts.pop(int(command[2]))
            name_of_gifts.insert(int(command[2]), command[1])
    elif command[0] == 'JustInCase':
        name_of_gifts.pop()
        name_of_gifts.append(command[1])

    command = input()

for el in name_of_gifts:
    if el == 'None':
        name_of_gifts.remove(el)

print(' '.join(name_of_gifts))
