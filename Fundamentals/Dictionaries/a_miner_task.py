iteration = 1
resources = {}
resource_to_add = ''

while True:

    command = input()

    if command == 'stop':
        break

    if iteration % 2 != 0:
        if command not in resources.keys():
            resources[command] = 0
            resource_to_add = command
        else:
            resource_to_add = command
    elif iteration % 2 == 0:
        resources[resource_to_add] += int(command)
    iteration += 1

for key, value in resources.items():
    print(f"{key} -> {value}")
