import re

data = input()
result = []
pattern = r'\d+'

while data:

    a = re.findall(pattern, data)
    result.extend(a)
    data = input()

print(*result, sep=' ')
