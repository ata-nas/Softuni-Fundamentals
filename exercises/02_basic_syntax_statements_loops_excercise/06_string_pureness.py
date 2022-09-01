total_strings = int(input())

pure_string = False
for _ in range(total_strings):
    user_string = input()
    if "," not in user_string \
            and "." not in user_string \
            and "_" not in user_string:
        print(f"{user_string} is pure.")
    else:
        print(f"{user_string} is not pure!")
