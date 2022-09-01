quantity_purchase = int(input())
days_to_christmas = int(input())

ornament_price, ornament_score = 2, 5
skirt_price, skirt_score = 5, 3
garland_price, garland_score = 3, 10
lights_price, lights_score = 15, 17

second_day_money = ornament_price
third_day_money = skirt_price + garland_price
fifth_day_money = lights_price

second_day_score = ornament_score
third_day_score = skirt_score + garland_score
fifth_day_score = lights_score

actual_qty_purchase = quantity_purchase
total_money = 0
total_spirit = 0
for day in range(2, days_to_christmas + 1):
    if day % 10 == 0:
        total_spirit -= 20
        total_money += 23  # second shopping from definition of exercise
    if day % 11 == 0:
        actual_qty_purchase += 2
    if day == days_to_christmas and day % 10 == 0:
        total_spirit -= 30
    if day % 2 == 0:
        if day % 3 == 0:
            if day % 5 == 0:
                total_money = total_money + actual_qty_purchase \
                              * (second_day_money + third_day_money + fifth_day_money)
                total_spirit = total_spirit \
                               + (second_day_score + third_day_score + fifth_day_score + 30)
                continue
            total_money = total_money + actual_qty_purchase * (second_day_money + third_day_money)
            total_spirit = total_spirit + (second_day_score + third_day_score)
            continue
        if day % 5 == 0:
            total_money = total_money + actual_qty_purchase * (second_day_money + fifth_day_money)
            total_spirit = total_spirit + (second_day_score + fifth_day_score)
            continue
        total_money = total_money + actual_qty_purchase * second_day_money
        total_spirit = total_spirit + second_day_score
        continue
    if day % 3 == 0:
        if day % 5 == 0:
            total_money = total_money + actual_qty_purchase * (third_day_money + fifth_day_money)
            total_spirit = total_spirit + (third_day_score + fifth_day_score + 30)  # as per definiton + 30 spirit
            continue
        total_money = total_money + actual_qty_purchase * third_day_money
        total_spirit = total_spirit + third_day_score
        continue
    if day % 5 == 0:
        total_money = total_money + actual_qty_purchase * fifth_day_money
        total_spirit = total_spirit + fifth_day_score

print(f"Total cost: {total_money}\n"
      f"Total spirit: {total_spirit}")
