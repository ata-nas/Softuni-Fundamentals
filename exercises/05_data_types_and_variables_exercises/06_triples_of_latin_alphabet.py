user_input = int(input())

for i in range(user_input):
    for j in range(user_input):
        for k in range(user_input):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
