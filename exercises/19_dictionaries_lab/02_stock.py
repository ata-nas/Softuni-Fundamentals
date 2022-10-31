user_input = input().split()

products_dict = {user_input[index]: user_input[index + 1] for index in range(0, len(user_input), 2)}

user_input_search = input().split()

for item in user_input_search:
    if item not in products_dict:
        print(f'Sorry, we don\'t have {item}')
    else:
        print(f"We have {products_dict.get(item)} of {item} left")
