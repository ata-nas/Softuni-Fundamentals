from itertools import product


def substrings(first_list: list, second_list: list):
    result = []
    for substring, string in product(first_list, second_list):
        if substring not in result and substring in string:
            result.append(substring)
    return result


user_input_first_list = list(input().split(sep=", "))
user_input_second_list = list(input().split(sep=", "))

result_list = substrings(user_input_first_list, user_input_second_list)

print(result_list)
