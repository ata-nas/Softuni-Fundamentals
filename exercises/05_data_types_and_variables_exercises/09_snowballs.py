snowball_count = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for _ in range(snowball_count):
    curr_weight = int(input())
    curr_time = int(input())
    curr_quality = int(input())
    value = (curr_weight / curr_time) ** curr_quality
    if value > best_value:
        best_weight = curr_weight
        best_time = curr_time
        best_quality = curr_quality
        best_value = int(value)

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
