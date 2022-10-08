company = {}


while True:

    command = input()

    if command == 'End':
        break

    name, emp_id = command.split(" -> ")

    if name not in company.keys():
        company[name] = [emp_id]
    else:
        if emp_id not in company[name]:
            company[name].append(emp_id)

for k, v in company.items():
    print(k)
    for el in v:
        print(f"-- {el}")
