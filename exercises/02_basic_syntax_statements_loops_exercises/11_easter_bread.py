budget = float(input())
price_flour_kg = float(input())

price_eggs_pack = price_flour_kg * 0.75
price_milk_dose = (price_flour_kg * 1.25) * 0.25

total_price_bread = price_flour_kg + price_eggs_pack + price_milk_dose

iteration_count = 1
bread_count = 0
eggs_amount = 0
money_left = budget
while money_left >= total_price_bread:
    eggs_amount += 3
    if iteration_count % 3 == 0:
        eggs_amount -= iteration_count - 2
    money_left -= total_price_bread
    iteration_count += 1
    bread_count += 1

print(
    f"You made {bread_count} loaves of Easter bread! Now you have {eggs_amount} eggs and {money_left:.2f}BGN left.")
