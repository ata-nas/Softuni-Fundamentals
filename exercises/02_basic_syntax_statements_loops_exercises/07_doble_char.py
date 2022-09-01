current_string = ""

while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for char in command:
        current_string += char * 2
    print(current_string)
    current_string = ""
