def perfect_number(number: int):
    result = ""
    digits_list = [num for num in range(1, number) if number % num == 0]
    if sum(digits_list) == number:
        result = "We have a perfect number!"
    else:
        result = "It's not so perfect."
    return result


user_input = int(input())

print(perfect_number(user_input))
