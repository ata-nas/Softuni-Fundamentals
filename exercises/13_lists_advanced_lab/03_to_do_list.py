user_list = [0] * 10

while True:
    user_command = input()
    if user_command == "End":
        break

    curr_command = user_command.split(sep="-")
    curr_priority = int(curr_command[0]) - 1
    curr_task = curr_command[1]

    user_list[curr_priority] = curr_task

result_list = [item for item in user_list if item != 0]

print(result_list)
