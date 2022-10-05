def multiplication_sing(numbers_list: list):
    minus_encounter = 0
    for item in numbers_list:
        if item == 0:
            return "zero"
        if item < 0:
            minus_encounter += 1
    return "negative" if minus_encounter % 2 != 0 else "positive"


first_number, second_number, third_number = int(input()), int(input()), int(input())

number_list = [first_number, second_number, third_number]

print(multiplication_sing(number_list))
