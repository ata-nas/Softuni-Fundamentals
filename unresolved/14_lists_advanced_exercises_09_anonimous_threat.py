#  Judge gives 90/100. There is some mistake in the functions, I do not know where.
#  I cannot think of pokemons_value test case where they do not pass,


def merge(command_list: list, target_list: list):
    start_index = int(command_list[1])
    end_index = int(command_list[2])

    merged_item = ''

    if start_index < 0:
        start_index == 0
    elif start_index > len(target_list) - 1:
        start_index = len(target_list) - 2

    if end_index > len(target_list) - 1:
        end_index = len(target_list) - 1

    merged_item = ''.join(target_list[start_index:end_index + 1])
    del target_list[start_index:end_index + 1]
    target_list.insert(start_index, merged_item)
    return target_list


def divide(command_list: list, target_list: list):
    index = int(command_list[1])
    partitions = int(command_list[2])

    target_item = target_list.pop(index)
    target_length = len(target_item)
    partition_size = target_length // partitions

    result_partition = []

    for item in range(partitions - 1):
        result_partition.append(target_item[:partition_size])
        target_item = target_item[partition_size:]

    result_partition.append(target_item)

    for item in result_partition[::-1]:
        target_list.insert(index, item)

    return target_list


user_input_list = input().split(sep=" ")

while True:
    user_command = input()
    if user_command == "3:1":
        break
    command = user_command.split(sep=" ")
    if command[0] == "merge":
        user_input_list = merge(command, user_input_list)
    if command[0] == "divide":
        user_input_list = divide(command, user_input_list)

print(*user_input_list)
