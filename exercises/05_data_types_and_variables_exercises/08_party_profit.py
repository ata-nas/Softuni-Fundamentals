group_size = int(input())
days_of_adventure = int(input())

coins_counter = 0
total_companions = group_size
for day in range(1, days_of_adventure + 1):
    if day % 10 == 0:
        total_companions -= 2
    if day % 15 == 0:
        total_companions += 5
    coins_counter += 50
    coins_counter -= 2 * total_companions
    if day % 3 == 0:
        coins_counter -= 3 * total_companions
    if day % 5 == 0:
        if day % 3 == 0:
            coins_counter -= 2 * total_companions
        coins_counter += 20 * total_companions

coin_per_companion = coins_counter // total_companions

print(f"{total_companions} companions received {coin_per_companion} coins each.")
