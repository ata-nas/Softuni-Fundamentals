gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    curr_command = command.split()
    if curr_command[0] == "OutOfStock":
        for index, gift in enumerate(gifts):
            if gift == curr_command[1]:
                gifts[index] = "None"
    elif curr_command[0] == "Required":
        if int(curr_command[2]) in range(len(gifts) - 1):
            gifts[int(curr_command[2])] = curr_command[1]
    elif curr_command[0] == "JustInCase":
        gifts.pop()
        gifts.append(curr_command[1])

for index, gift in enumerate(gifts):
    if gift == "None":
        gifts.pop(index)

for index, gift in enumerate(gifts):
    if index == len(gifts) - 1:
        print(gifts[index])
        break
    print(gifts[index], end=" ")
