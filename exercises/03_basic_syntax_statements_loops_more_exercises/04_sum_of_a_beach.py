user_input = input()

current_string = user_input.lower()

counter_sand = current_string.count("sand")
counter_water = current_string.count("water")
counter_fish = current_string.count("fish")
counter_sun = current_string.count("sun")

all_count = counter_sand + counter_water + counter_fish + counter_sun

print(all_count)
