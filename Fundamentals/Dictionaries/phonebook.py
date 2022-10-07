phonebook = {}
iterations = 0

while True:

    command = input()

    if command.isdigit():
        iterations = int(command)
        break

    name, number = command.split('-')

    phonebook[name] = number

for _ in range(iterations):

    name = input()

    if name not in phonebook.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
