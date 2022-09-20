user_input = [int(i) for i in input().split()]
nums_to_remove = int(input())

sorted_list = sorted(user_input)

for index in range(nums_to_remove):
    user_input.remove(sorted_list[index])

for index, item in enumerate(user_input):
    if index + 1 == len(user_input):
        print(item)
        break
    print(item, end=", ")
