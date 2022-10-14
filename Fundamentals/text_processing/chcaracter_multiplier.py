string_1, string_2 = input().split()

result = 0
index = 0

if len(string_1) > len(string_2):
    index = len(string_2)
    for i in range(0, index):
        result += ord(string_1[i]) * ord(string_2[i])
    for e in range(index, len(string_1)):
        result += ord(string_1[e])

elif len(string_2) > len(string_1):
    index = len(string_1)
    for i in range(0, index):
        result += ord(string_1[i]) * ord(string_2[i])
    for e in range(index, len(string_2)):
        result += ord(string_2[e])
else:
    index = len(string_1)
    for i in range(0, index):
        result += ord(string_1[i]) * ord(string_2[i])

print(result)
