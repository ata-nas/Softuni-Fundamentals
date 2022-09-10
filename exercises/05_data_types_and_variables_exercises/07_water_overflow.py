filling_range = int(input())

total_capacity = 255
total_in_tank = 0

for _ in range(filling_range):
    qty_current_fill = int(input())
    if total_capacity >= qty_current_fill:
        total_capacity -= qty_current_fill
        total_in_tank += qty_current_fill
    else:
        print("Insufficient capacity!")

print(total_in_tank)
ß