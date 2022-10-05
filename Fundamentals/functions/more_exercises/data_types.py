def data_type(dt, value):
    result = None
    if dt == "int":
        result = int(value) * 2
    elif dt == "real":
        result = f"{(float(value) * 1.5):.2f}"
    elif dt == "string":
        result = f"${value}$"

    return result


print(data_type(input(), input()))
