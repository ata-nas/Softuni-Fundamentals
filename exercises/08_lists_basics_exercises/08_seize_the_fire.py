FIRE_RANGE_HIGH = range(81, 125 + 1)
FIRE_RANGE_MEDIUM = range(51, 80 + 1)
FIRE_RANGE_LOW = range(1, 50 + 1)


def is_valid(list_commands):
    curr_command = list_commands.split(sep=" = ")
    return (curr_command[0] == "High" and int(curr_command[1]) in FIRE_RANGE_HIGH) \
        or (curr_command[0] == "Medium" and int(curr_command[1]) in FIRE_RANGE_MEDIUM) \
        or (curr_command[0] == "Low" and int(curr_command[1]) in FIRE_RANGE_LOW)


cells = input().split(sep="#")
water = int(input())

total_effort = 0
water_left = water

print("Cells:")
for command in cells:
    current_command = command.split(sep=" = ")
    current_fire_value = int(current_command[1])
    if water_left < current_fire_value:
        continue
    if is_valid(command):
        water_left -= current_fire_value
        total_effort += current_fire_value * 0.25
        print(f" - {current_fire_value}")

total_fire = water - water_left

print(f"Effort: {total_effort:.2f}\n"
      f"Total Fire: {total_fire}")
