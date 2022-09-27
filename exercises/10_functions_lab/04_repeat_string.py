def result(string: str, multiplier: int): return user_string * repeating


user_string = input()
repeating = int(input())

print(result(user_string, repeating))


# Alternative solution
# 
# user_string = input()
# repeating = int(input())
#
# repeat_string = lambda a, b: user_string * repeating
#
# result = repeat_string(user_string, repeating)
#
# print(result)
