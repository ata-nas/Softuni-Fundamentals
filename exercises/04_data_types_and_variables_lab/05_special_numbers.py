user_input = int(input())

for n in range(1, user_input + 1):
    sum_of_digits = 0
    digit = n
    while digit != 0:
        current_digit = digit % 10
        sum_of_digits += current_digit
        digit = int(digit / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
