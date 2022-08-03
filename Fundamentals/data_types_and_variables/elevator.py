number_of_people = int(input())
capacity = int(input())
courses = 0

while number_of_people:

    if number_of_people <= 0:
        break

    number_of_people -= capacity
    courses += 1

print(courses)
