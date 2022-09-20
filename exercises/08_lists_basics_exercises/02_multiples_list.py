factor = int(input())
count = int(input())

user_list = [item * factor for item in range(1, count + 1)]

print(user_list)
