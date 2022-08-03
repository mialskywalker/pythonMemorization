first_char = int(input())
last_char = int(input())

loop = last_char - first_char
result = ""

for i in range(loop + 1):

    num_to_use = chr(first_char + i)
    result += num_to_use + " "

print(result)
