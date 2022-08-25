total_numbers = int(input())

all_are_even = True
odd_number = 0
for _ in range(total_numbers):
    current_num = int(input())
    if current_num % 2 == 0:
        continue
    all_are_even = False
    odd_number += current_num
    break

if all_are_even:
    print("All numbers are even.")
else:
    print(f"{odd_number} is odd!")
