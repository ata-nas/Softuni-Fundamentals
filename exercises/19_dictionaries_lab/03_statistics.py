inventory = {}

while True:
    user_input = input()
    if user_input == "statistics":
        break
    user_input = user_input.split(sep=": ")
    key = user_input[0]
    value = int(user_input[1])
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value

print('Products in stock:')

for key, value in inventory.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
