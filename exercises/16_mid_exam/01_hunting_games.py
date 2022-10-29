days_of_adventure = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water_supplies = days_of_adventure * number_of_players * water_per_day_per_person
total_food_supplies = days_of_adventure * number_of_players * food_per_day_per_person

energy_enough = True
for day in range(1, days_of_adventure + 1):
    energy_needed_today = float(input())
    group_energy -= energy_needed_today
    if group_energy <= 0:
        energy_enough = False
        break
    if day % 2 == 0:
        group_energy = group_energy + (group_energy * 0.05)
        total_water_supplies = total_water_supplies - (total_water_supplies * 0.30)
    if day % 3 == 0:
        total_food_supplies = total_food_supplies - (total_food_supplies / number_of_players)
        group_energy = group_energy + (group_energy * 0.10)

if energy_enough:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(
        f"You will run out of energy. You will be left with {total_food_supplies:.2f} food and {total_water_supplies:.2f} water.")
