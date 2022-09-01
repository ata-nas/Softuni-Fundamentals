forbidden_name = False

while not forbidden_name:
    command = input()

    if command == "Voldemort":
        forbidden_name = True
        break

    result = ""
    if command == "Welcome!":
        break
    elif len(command) < 5:
        result = f"{command} goes to Gryffindor."
    elif len(command) == 5:
        result = f"{command} goes to Slytherin."
    elif len(command) == 6:
        result = f"{command} goes to Ravenclaw."
    else:
        result = f"{command} goes to Hufflepuff."
    print(result)

if forbidden_name:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
