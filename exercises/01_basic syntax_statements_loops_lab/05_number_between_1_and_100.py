in_range = True
final_number = 0

while in_range:
    number = float(input())
    if not 1 <= number <= 100:
        continue
    in_range = False
    final_number = number
    break

print(f"The number {final_number} is between 1 and 100")
