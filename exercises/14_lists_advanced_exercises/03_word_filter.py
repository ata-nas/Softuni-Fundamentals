user_list = [item for item in input().split(sep=" ") if len(item) % 2 == 0]

for word in user_list:
    print(word)
