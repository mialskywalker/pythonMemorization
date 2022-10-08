courses = {}


while True:

    command = input()

    if command == 'end':
        break

    course, name = command.split(' : ')

    if course not in courses.keys():
        courses[course] = [name]
    else:
        courses[course].append(name)

for k, v in courses.items():

    print(f"{k}: {len(v)}")
    for el in v:
        print(f"-- {el}")
