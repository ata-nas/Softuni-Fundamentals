user_input = list(sorted(input().split(sep=", "), key=lambda x: (-len(x), x)))

print(user_input)
