MAX_VALUE_CLOTHES = 50.00
MAX_VALUE_SHOES = 35.00
MAX_VALUE_ACCESSORIES = 20.50


def valid_price(command):
    curr_command = command.split(sep="->")
    return (curr_command[0] == "Clothes" and float(curr_command[1]) <= MAX_VALUE_CLOTHES) \
        or (curr_command[0] == "Shoes" and float(curr_command[1]) <= MAX_VALUE_SHOES) \
        or (curr_command[0] == "Accessories" and float(curr_command[1]) <= MAX_VALUE_ACCESSORIES)


items_list = input().split(sep="|")
budget = float(input())

current_budget = budget
sum_of_purchases = 0
profit = 0
result = ""

for purchase in items_list:
    current_purchase = purchase.split(sep="->")
    current_item, current_price = current_purchase[0], float(current_purchase[1])
    if current_price > current_budget or not valid_price(purchase):
        continue
    current_budget -= current_price
    sum_of_purchases += current_price
    markup = current_price * 0.40
    profit += markup
    print(f"{(current_price + markup):.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

total_money = sum_of_purchases + profit + current_budget

if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
