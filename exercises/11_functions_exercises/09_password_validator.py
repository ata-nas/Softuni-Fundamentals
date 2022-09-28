def valid_password(password: str):
    result = []
    if not 6 <= len(password) <= 10:
        result.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        result.append("Password must consist only of letters and digits")
    digits_in_password = 0
    for item in password:
        if item.isnumeric():
            digits_in_password += 1
        if digits_in_password == 2:
            break
    if digits_in_password != 2:
        result.append("Password must have at least 2 digits")
    return result


user_input = input()

if valid_password(user_input):
    for item in valid_password(user_input):
        print(item)
else:
    print("Password is valid")
