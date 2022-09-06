user_input = input()

sheep_list = user_input.split(sep=", ")
rev_list = sheep_list[::-1]

if rev_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index, animal in enumerate(rev_list):
        if animal == "wolf":
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
