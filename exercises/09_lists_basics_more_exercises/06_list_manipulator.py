from sys import maxsize

EXCHANGE_COMMAND = "exchange"
MAX_COMMAND = "max"
MIN_COMMAND = "min"
FIRST_COMMAND = "first"
LAST_COMMAND = "last"
END_COMMAND = "end"


def exchange(user_list, index):
    if index < 0 or index > len(user_list) - 1:
        return "Invalid index"  # possible error, depends if judge wants to print in case negative num
    return user_list[index + 1:] + user_list[:index + 1]


def max_even_odd(user_list, command):
    max_num = -maxsize
    max_num_index = 0
    if command == "even":
        for index, item in enumerate(user_list):
            if item % 2 == 0 and item >= max_num:
                max_num = item
                max_num_index = index
    elif command == "odd":
        for index, item in enumerate(user_list):
            if item % 2 != 0 and item >= max_num:
                max_num = item
                max_num_index = index
    if max_num == -maxsize:
        return "No matches"
    return max_num_index


def min_even_odd(user_list, command):
    min_num = maxsize
    min_num_index = 0
    if command == "even":
        for index, item in enumerate(user_list):
            if item % 2 == 0 and item <= min_num:
                min_num = item
                min_num_index = index
    if command == "odd":
        for index, item in enumerate(user_list):
            if item % 2 != 0 and item <= min_num:
                min_num = item
                min_num_index = index
    if min_num == maxsize:
        return "No matches"
    return min_num_index


def first_count_even_odd(user_list, count, curr_command):
    result_list = []
    if count > len(user_list):
        return "Invalid count"
    if curr_command == "even":
        for item in user_list:
            if item % 2 == 0:
                result_list.append(item)
            if len(result_list) == count:
                break
    elif curr_command == "odd":
        for item in user_list:
            if item % 2 != 0:
                result_list.append(item)
            if len(result_list) == count:
                break
    return result_list


def last_count_even_odd(user_list, count, curr_command):
    result_list = []
    if count > len(user_list):
        return "Invalid count"
    if curr_command == "even":
        for item in user_list:
            if item % 2 == 0:
                result_list.append(item)
    elif curr_command == "odd":
        for item in user_list:
            if item % 2 != 0:
                result_list.append(item)
    return result_list[-count:]


user_input = [int(i) for i in input().split(sep=" ")]

current_list = list(user_input)

while True:
    user_command = input()
    if user_command == END_COMMAND:
        print(current_list)
        break
    result = ""
    command = list(user_command.split(sep=" "))
    if command[0] == EXCHANGE_COMMAND:
        if exchange(current_list, int(command[1])) == "Invalid index":
            result = exchange(current_list, int(command[1]))
        else:
            current_list = exchange(current_list, int(command[1]))
    elif command[0] == MAX_COMMAND:
        result = max_even_odd(current_list, command[1])
    elif command[0] == MIN_COMMAND:
        result = min_even_odd(current_list, command[1])
    elif command[0] == FIRST_COMMAND:
        result = first_count_even_odd(current_list, int(command[1]), command[2])
    elif command[0] == LAST_COMMAND:
        result = last_count_even_odd(current_list, int(command[1]), command[2])
    if result == "":
        continue
    print(result)
