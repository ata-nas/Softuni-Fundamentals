lost_games = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

second_shield_break = 0

for game in range(2, lost_games + 1):
    if game % 2 == 0:
        broken_helmet_count += 1
    if game % 3 == 0:
        broken_sword_count += 1
    if game % 2 == 0 and game % 3 == 0:
        broken_shield_count += 1
        second_shield_break += 1
        if second_shield_break == 2:
            second_shield_break = 0
            broken_armor_count += 1

total_cost = (broken_helmet_count * helmet_price) + \
             (broken_sword_count * sword_price) + \
             (broken_shield_count * shield_price) + \
             (broken_armor_count * armor_price)

print(f"Gladiator expenses: {total_cost:.2f} aureus")
