import string

VALID_COMMANDS = ['Make Upper', 'Make Lower', 'Insert', 'Replace', 'Validation']


user_input = input()

password = [item for item in user_input]

while True:
    user_command = input()

    if user_command == 'Complete':
        break

    command_type = ''
    for item in VALID_COMMANDS:
        if item in user_command:
            command_type = item
            break
    else:
        continue

    if command_type == 'Make Upper':
        index = int(user_command.split()[2])
        if index > len(password) - 1:
            continue
        password[index] = password[index].upper()
        print(''.join(password))
    elif command_type == 'Make Lower':
        index = int(user_command.split()[2])
        if index > len(password) - 1:
            continue
        password[index] = password[index].lower()
        print(''.join(password))
    elif command_type == 'Insert':
        index = int(user_command.split()[1])
        if index > len(password) - 1:
            continue
        char = user_command.split()[2]
        password.insert(index, char)
        print(''.join(password))
    elif command_type == 'Replace':
        char = user_command.split()[1]
        value = int(user_command.split()[2])
        ascii_value_char = ord(char)
        char_in_password = False
        for index, item in enumerate(password):
            if item == char:
                char_in_password = True
                password[index] = chr(ascii_value_char + value)
        if char_in_password:
            print(''.join(password))
    elif command_type == 'Validation':
        check_pass = ''.join(password)
        valid_symbols = '_' + string.ascii_letters + string.digits
        if len(check_pass) < 8:
            print('Password must be at least 8 characters long!')

        if any(char not in valid_symbols for char in check_pass):
            print('Password must consist only of letters, digits and _!')

        if not any(char in string.ascii_uppercase for char in check_pass):
            print('Password must consist at least one uppercase letter!')

        if not any(char in string.ascii_lowercase for char in check_pass):
            print('Password must consist at least one lowercase letter!')

        if not any(char in string.digits for char in check_pass):
            print('Password must consist at least one digit!')