def rectangle(length, width):
    def area(a, b):
        return a * b

    def perimeter(a, b):
        return 2 * a + 2 * b

    if type(length) == int and type(width) == int:
        return f"Rectangle area: {area(length, width)}\n" \
               f"Rectangle perimeter: {perimeter(length, width)}"
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
