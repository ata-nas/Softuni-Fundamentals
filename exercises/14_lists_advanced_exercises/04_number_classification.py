user_input_list = input().split(sep=", ")

print("Positive:", ", ".join([item for item in user_input_list if int(item) >= 0]))
print("Negative:", ", ".join([item for item in user_input_list if int(item) < 0]))
print("Even:", ", ".join([item for item in user_input_list if int(item) % 2 == 0]))
print("Odd:", ", ".join([item for item in user_input_list if int(item) % 2 != 0]))
