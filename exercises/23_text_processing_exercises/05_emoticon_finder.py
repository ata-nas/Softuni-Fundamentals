user_input = input()

for index in range(len(user_input)):
    char = user_input[index]
    if char == ":":
        print(char + user_input[index + 1])
