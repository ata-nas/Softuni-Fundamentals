lower_case_commands = ["coding", "dog", "cat", "movie"]  # base list with possible commands
upper_case_commands = [item.upper() for item in lower_case_commands]

#  a more readable way to represent the list comprehension above
# upper_case_commands = []
# for item in lower_case_commands:
#     upper_case_commands.append(item.upper())

coffee_counter = 0
sleep_needed = False
while not sleep_needed:
    command = input()
    if command == "END":
        break
    if command in lower_case_commands:
        coffee_counter += 1
    elif command in upper_case_commands:
        coffee_counter += 2
    if coffee_counter > 5:
        sleep_needed = True
        break

if sleep_needed:
    print("You need extra sleep")
else:
    print(coffee_counter)
