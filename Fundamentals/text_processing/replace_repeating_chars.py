data = input()

result = ''

for i in range(0, len(data)):
    if i == len(data) - 1:
        result += data[i]
    else:
        if data[i] != data[i+1]:
            result += data[i]

print(result)
