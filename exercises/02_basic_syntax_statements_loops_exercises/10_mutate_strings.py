first_string = input()
second_string = input()

prev_result = first_string
for index, char in enumerate(second_string):
    result = prev_result
    if char != prev_result[index]:
        result = prev_result[:index] + char + prev_result[index + 1:]
        print(result)
    prev_result = result
