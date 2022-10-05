first_string = input().split(', ')
second_string = input().split(', ')

result = []

for word in first_string:
    for el in second_string:
        if word in el:
            if word not in result:
                result.append(word)

print(result)
