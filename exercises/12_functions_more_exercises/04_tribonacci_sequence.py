def tribonacci_sequence(items: int):
    result_list = [1, 1, 2]
    curr_index = 2

    if items == 0:
        return ""
    elif items == 1:
        return result_list[:curr_index -1]
    elif items == 2:
        return result_list[:curr_index]

    while len(result_list) < items:
        curr_num = result_list[curr_index] + result_list[curr_index - 1] + result_list[curr_index - 2]
        result_list.append(curr_num)
        curr_index += 1

    return result_list


user_input_number_of_items = (int(input()))

for item in tribonacci_sequence(user_input_number_of_items):
    print(item, end=" ")
