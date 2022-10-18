encrypted_message = input()
result = [el for el in encrypted_message]

while True:

    command = input().split('|')

    if command[0] == 'Decode':
        break

    if command[0] == 'Move':
        num_of_letters = int(command[1])
        for i in range(num_of_letters):
            result.append(result[i])
        for _ in range(num_of_letters):
            result.pop(0)

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]

        result.insert(index, value)

    elif command[0] == 'ChangeAll':
        first = command[1]
        second = command[2]

        for i in range(len(result)):
            if first == result[i]:
                result[i] = second

print(f"The decrypted message is: {''.join(result)}")
