user_input = input()

result = user_input[0]

for char in user_input:
    if char != result[-1]:
        result += char

print(result)
