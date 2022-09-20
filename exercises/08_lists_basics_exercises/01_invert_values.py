user_input = input()

user_list = user_input.split()
opposites_list = []
for item in user_list:
    reverse_value = int(item) * -1
    opposites_list.append(reverse_value)

print(opposites_list)
