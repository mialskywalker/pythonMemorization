def validator(password):
    result = ''
    num_of_digits = 0
    first_validation = True
    second_validation = True
    third_validation = True

    if len(password) < 6 or len(password) > 10:
        result += "Password must be between 6 and 10 characters\n"
        first_validation = False
    if not password.isalnum():
        result += "Password must consist only of letters and digits\n"
        second_validation = False
    for el in password:
        if el.isdigit():
            num_of_digits += 1

    if num_of_digits < 2:
        result += "Password must have at least 2 digits"
        third_validation = False

    if first_validation and second_validation and third_validation:
        result = "Password is valid"

    return result


print(validator(input()))
