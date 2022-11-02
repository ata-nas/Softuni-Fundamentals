def odd_occurances_lower(input_list: list) -> list:
    curr_dict = {}

    for item in input_list:
        curr_item = item.lower()

        if curr_item not in curr_dict.keys():
            curr_dict[curr_item] = 1

        else:
            curr_dict[curr_item] += 1

    result_list = []  # [key for key, value in curr_dict.items() if value % 2 != 0 and key not in result_list]

    for key, value in curr_dict.items():
        if key in result_list:
            continue

        if value % 2 != 0:
            result_list.append(key)

    return result_list


def main():
    user_input = input().split(sep=" ")

    result = odd_occurances_lower(user_input)

    print(*result)


if __name__ == '__main__':
    main()
