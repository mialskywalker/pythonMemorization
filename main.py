while True:

    text = input()
    result = ""

    if text == "End":
        break
    elif text == "SoftUni":
        pass
    else:
        for ch in text:
            for el in ch:
                result += 2 * el
        print(result)
