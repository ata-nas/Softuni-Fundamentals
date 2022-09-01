first_string = input()
second_string = input()

str_a = first_string
str_b = second_string

prev_result = str_a
for index, char in enumerate(str_b):
    result = prev_result
    if char != prev_result[index]:
        result = prev_result[:index] + char + prev_result[index + 1:]
        print(result)
    prev_result = result
