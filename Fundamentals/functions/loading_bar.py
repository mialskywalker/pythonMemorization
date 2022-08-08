def loading_bar(number):

    bar = ['.' for _ in range(10)]

    percentage = number // 10

    for _ in range(percentage):
        bar.pop()
        bar.insert(0, '%')

    if '.' not in bar:
        result = f"100% Complete!\n" \
                 f"[{''.join(bar)}]"
    else:
        result = f"{number}% [{''.join(bar)}]\n" \
                 f"Still loading..."

    return result


print(loading_bar(int(input())))
