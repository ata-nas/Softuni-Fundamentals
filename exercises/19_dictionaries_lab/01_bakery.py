user_input = input().split()

products_dict = {user_input[index]: int(user_input[index + 1]) for index in range(0, len(user_input), 2)}

# products_dict = dict()
# for index in range(0, len(user_input), 2):
#     products_dict[user_input[index]] = int(user_input[index + 1])

print(products_dict)
