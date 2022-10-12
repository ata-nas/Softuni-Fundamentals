user_input_rooms = int(input())

enough_chairs = True
free_chairs_left = 0
for room in range(1, user_input_rooms + 1):
    user_input_current_room = input().split(sep=" ")
    chairs = len(user_input_current_room[0])
    visitors = int(user_input_current_room[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        enough_chairs = False
        continue
    free_chairs_left += chairs - visitors

if enough_chairs:
    print(f"Game On, {free_chairs_left} free chairs left")
