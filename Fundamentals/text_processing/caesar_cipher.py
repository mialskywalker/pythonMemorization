text = input()

result = ''

for el in text:

    result += chr(ord(el)+3)

print(result)
