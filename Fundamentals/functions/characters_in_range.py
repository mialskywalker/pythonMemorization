def chars_in_range(first, second):

    chars = []

    for i in range(ord(first)+1, ord(second)):
        chars.append(chr(i))

    return ' '.join(chars)


print(chars_in_range(input(), input()))
