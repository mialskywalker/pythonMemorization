seats = 0
name = ""
total_tickets = 0
total_student = 0
total_kid = 0
total_standard = 0
command = ""

while True:
    taken_seats = 0
    standard = 0
    kid = 0
    student = 0

    if command == "Finish":
        break
    command = input()
    if command == "Finish":
        break

    elif command != "End":
        name = command
        seats = int(input())

    while True:
        command = input()
        if command == "End":
            break
        if seats == taken_seats:
            break
        else:
            if command == "standard":
                standard += 1
            elif command == "kid":
                kid += 1
            elif command == "student":
                student += 1
            taken_seats += 1
    total_tickets += taken_seats
    total_student += student
    total_kid += kid
    total_standard += standard

    print(f"{name} - {((taken_seats / seats) * 100):.2f}% full.")

print(f"Total tickets: {total_tickets}\n"
      f"{((total_student / total_tickets) * 100):.2f}% student tickets.\n"
      f"{((total_standard / total_tickets) * 100):.2f}% standard tickets.\n"
      f"{((total_kid / total_tickets) * 100):.2f}% kids tickets.\n")
