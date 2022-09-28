def odd_even_sum(user_number: int):
    evens_list = []
    odds_list = []
    curr_number = user_number
    for _ in range(len(str(curr_number))):
        curr_digit = curr_number % 10
        if curr_digit % 2 == 0:
            evens_list.append(curr_digit)
        else:
            odds_list.append(curr_digit)
        curr_number //= 10
    sum_evens = sum(evens_list)
    sum_odds = sum(odds_list)
    return [sum_evens, sum_odds]


user_input = int(input())

sum_results = odd_even_sum(user_input)

print(f"Odd sum = {sum_results[1]}, Even sum = {sum_results[0]}")
