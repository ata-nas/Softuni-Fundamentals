from sys import maxsize

largest_number = -maxsize

for number in range(3):
    user_input = int(input())
    if user_input > largest_number:
        largest_number = user_input

print(largest_number)
