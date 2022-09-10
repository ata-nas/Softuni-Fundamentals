user_range = int(input())

ascii_value_sum = 0

for _ in range(user_range):
    current_char = ord(input())
    ascii_value_sum += current_char

print(f"The sum equals: {ascii_value_sum}")
