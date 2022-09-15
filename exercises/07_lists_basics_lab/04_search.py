lines = int(input())
user_filter = input()

strings_list = []

for _ in range(lines):
    user_string = input()
    strings_list.append(user_string)

filtered_list = []

for item in strings_list:
    if user_filter in item:
        filtered_list.append(item)

print(strings_list)
print(filtered_list)
