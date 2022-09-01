divisor = int(input())
boundary = int(input())

current_num = 0

for number in range(1, boundary + 1):
    if number % divisor == 0:
        current_num = number

print(current_num)
