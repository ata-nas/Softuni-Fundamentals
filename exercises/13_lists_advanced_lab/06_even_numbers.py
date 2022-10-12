def evens_indices(numbers_list: list):
    indices_list = list(map(lambda x: x if numbers_list[x] % 2 == 0 else "no", range(len(numbers_list))))
    return list(filter(lambda res: res != "no", indices_list))


user_input = list(map(int, input().split(sep=", ")))
print(evens_indices(user_input))
