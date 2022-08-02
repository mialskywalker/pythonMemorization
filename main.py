first_string = input()
second_string = input()
result = ""

for i in range(len(first_string)):

    result = first_string

    first_string = first_string.replace(first_string[i], second_string[i], 1)

    if result != first_string:
        print(first_string)
    else:
        continue
