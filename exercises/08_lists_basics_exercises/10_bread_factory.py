ENERGY_START = 100
COINS_START = 100

events_list = input().split(sep="|")

energy = ENERGY_START
coins = COINS_START
day_successful = True

for event in events_list:
    curr_event = event.split(sep="-")
    curr_task = curr_event[0]
    curr_value = int(curr_event[1])
    if curr_task == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            coins += curr_value
            energy -= 30
            print(f"You earned {curr_value} coins.")
    elif curr_task == "rest":
        if curr_value + energy >= 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += curr_value
            print(f"You gained {curr_value} energy.")
        print(f"Current energy: {energy}.")
    elif curr_value <= coins:
        coins -= curr_value
        print(f"You bought {curr_task}.")
    else:
        day_successful = False
        print(f"Closed! Cannot afford {curr_task}.")
        break

if day_successful:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")
