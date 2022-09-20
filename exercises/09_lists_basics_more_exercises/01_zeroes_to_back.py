user_list = [int(item) for item in input().split(sep=", ")]

result_list = list(user_list)

for item in user_list:
    if item == 0:
        result_list.remove(item)
        result_list.append(item)

print(result_list)
