cars_list = [item for item in input().split(sep=">>")]

car_types = ["family", "heavyDuty", "sports"]

total_tax = 0

for item in cars_list:
    item = item.split(sep=" ")

    if item[0] not in car_types:
        print("Invalid car type.")
        continue

    if item[0] == car_types[0]:  # family type car
        tax = 50
        tax -= int(item[1]) * 5
        tax += (int(item[2]) // 3000) * 12
        total_tax += tax
        print(f"A {item[0]} car will pay {tax:.2f} euros in taxes.")
    elif item[0] == car_types[1]:  # heavyDuty type car
        tax = 80
        tax -= int(item[1]) * 8
        tax += (int(item[2]) // 9000) * 14
        total_tax += tax
        print(f"A {item[0]} car will pay {tax:.2f} euros in taxes.")
    elif item[0] == car_types[2]:  # family type car
        tax = 100
        tax -= int(item[1]) * 9
        tax += (int(item[2]) // 2000) * 18
        total_tax += tax
        print(f"A {item[0]} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
