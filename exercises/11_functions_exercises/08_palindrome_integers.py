def palindrome_number(number: str):
    digits_list = list(number)
    return digits_list == list(reversed(digits_list))


user_input = list(input().split(sep=", "))

for item in user_input:
    if palindrome_number(item):
        print("True")
    else:
        print("False")
