user_string = input()

# Using list comprehension
# capitals_index_list = [index for index, char in enumerate(user_string) if char.isupper()]

capitals_index_list = []

for index, char in enumerate(user_string):
    if char.isupper():
        capitals_index_list.append(index)

print(capitals_index_list)
