lines = int(input())

user_string = ""

for _ in range(lines):
    user_input = input()
    user_string += "".join(user_input)

stack = []

for char in user_string:
    if char == "(":
        stack.append(char)
        if len(stack) >= 2:  # nested brackets don't count and are excluded.
            break
    elif char == ")":
        if not stack:
            stack.append(char)
            break
        stack.pop()

if stack:
    print("UNBALANCED")
else:
    print("BALANCED")
