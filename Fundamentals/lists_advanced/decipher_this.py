text = input().split()

result = []
ind = 0
word = ''
digit = ''
second = ''
last = ''

for w in text:
    word = ''
    for el in w:
        if el.isdigit():
            digit += el
            ind += 1
    word += chr(int(digit))
    word += w[ind:]
    word = list(word)
    second = word[1]
    last = word[-1]
    word[1] = last
    word[-1] = second
    word = "".join(word)
    result.append(word)

    digit = ''
    ind = 0

print(" ".join(result))
