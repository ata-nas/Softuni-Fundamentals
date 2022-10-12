def average_happy_people(user_list: list, user_factor: int):
    happiness_with_factor_list = list(map(lambda x: x * user_factor, user_list))

    result_list = list(filter(lambda x: x >= sum(happiness_with_factor_list) / len(happiness_with_factor_list),
                              happiness_with_factor_list))

    return f"Score: {len(result_list)}/{len(user_list)}. Employees are happy!" \
        if len(result_list) >= (len(user_list) // 2) \
        else f"Score: {len(result_list)}/{len(user_list)}. Employees are not happy!"


user_input_list = [int(num) for num in input().split(sep=" ")]
user_input_factor = int(input())

print(average_happy_people(user_input_list, user_input_factor))
