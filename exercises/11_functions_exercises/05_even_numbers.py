user_input = [int(item) for item in input().split(sep=" ")]

result = list(filter(lambda x: x % 2 == 0, user_input))

print(result)
