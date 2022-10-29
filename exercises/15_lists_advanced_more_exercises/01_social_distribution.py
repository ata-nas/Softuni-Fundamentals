def distribute_wealth(population_list: list, min_wealth: int):
    items_in_pop_list = len(population_list)
    sum_wealth_to_distribute = sum(population_list) - (items_in_pop_list * min_wealth)

    if sum_wealth_to_distribute < 0:
        return f"No equal distribution possible"

    # current highest location to use first

    for item_index, item_value in enumerate(population_list):
        if item_value >= min_wealth:  # check if item_value needs redistributing of wealth
            continue

        max_pop_index = population_list.index(max(population_list))
        sum_needed_to_redistribute = min_wealth - item_value
        left_to_redistribute_currently = population_list[max_pop_index] - min_wealth

        if sum_needed_to_redistribute <= left_to_redistribute_currently:
            population_list[max_pop_index] -= sum_needed_to_redistribute
            population_list[item_index] += sum_needed_to_redistribute
        else:
            while population_list[item_index] != min_wealth:
                if left_to_redistribute_currently - sum_needed_to_redistribute >= 0:
                    population_list[max_pop_index] -= sum_needed_to_redistribute
                    population_list[item_index] += sum_needed_to_redistribute
                    break

                population_list[max_pop_index] -= left_to_redistribute_currently
                population_list[item_index] += left_to_redistribute_currently

                max_pop_index = population_list.index(max(population_list))

    return population_list


population = [int(num) for num in input().split(sep=", ")]

minimum_wealth = int(input())

print(distribute_wealth(population, minimum_wealth))
