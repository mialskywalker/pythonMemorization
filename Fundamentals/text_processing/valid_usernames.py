text = input().split(', ')

is_valid = False

for el in text:

    if 3 <= len(el) <= 16:
        for i in el:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or i.isdigit() or i == '-' or i == '_':
                is_valid = True
            else:
                is_valid = False
                break
        if is_valid:
            print(el)
