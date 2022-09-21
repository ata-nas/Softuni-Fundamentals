number_sequence = input().split(sep=" ")

left_car = [int(time) for time in number_sequence[:int((len(number_sequence) - 1) / 2)]]
right_car = [int(time) for time in number_sequence[int((len(number_sequence) + 1) / 2):]]

total_time_left = 0
total_time_right = 0

if 0 not in left_car:
    for time in left_car:
        total_time_left += time
else:
    stack_left_car = list(reversed(left_car))
    curr_time_before_zero_encounter = 0
    while stack_left_car:
        if stack_left_car[-1] == 0:
            total_time_left += curr_time_before_zero_encounter * 0.8
            curr_time_before_zero_encounter = 0
            stack_left_car.pop()
            continue
        curr_time_before_zero_encounter += stack_left_car[-1]
        stack_left_car.pop()
    if curr_time_before_zero_encounter:
        total_time_left += curr_time_before_zero_encounter

if 0 not in right_car:
    for time in right_car:
        total_time_right += time
else:
    stack_right_car = list(right_car)
    curr_time_before_zero_encounter = 0
    while stack_right_car:
        if stack_right_car[-1] == 0:
            total_time_right += curr_time_before_zero_encounter * 0.8
            curr_time_before_zero_encounter = 0
            stack_right_car.pop()
            continue
        curr_time_before_zero_encounter += stack_right_car[-1]
        stack_right_car.pop()
    if curr_time_before_zero_encounter:
        total_time_right += curr_time_before_zero_encounter

if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")
