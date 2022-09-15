COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

lines = int(input())

inputs_list = []
filtered_list = []

for _ in range(lines):
    user_input = int(input())
    inputs_list.append(user_input)

command = input()

for item in inputs_list:
    filter_command = (
            (command == COMMAND_EVEN and item % 2 == 0) or
            (command == COMMAND_ODD and item % 2 != 0) or
            (command == COMMAND_NEGATIVE and item < 0) or
            (command == COMMAND_POSITIVE and item >= 0)
    )
    if filter_command:
        filtered_list.append(item)

print(filtered_list)
