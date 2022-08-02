result = 0

while True:

    command = input()

    if command == "END":
        break
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        result += 2
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        result += 1

if result > 5:
    print("You need extra sleep")
else:
    print(result)
