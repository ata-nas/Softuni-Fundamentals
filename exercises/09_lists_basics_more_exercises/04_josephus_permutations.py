initial_sequence = [int(person) for person in input().split(sep=" ")]
k = int(input())

curr_people = list(initial_sequence)
result_list = []

index = (k % len(curr_people)) - 1
print("[", end="")
while curr_people:
    if len(curr_people) == 1:
        curr_print = curr_people.pop(index)
        print(curr_print, end="]")
        break
    curr_print = curr_people.pop(index)
    print(curr_print, end=",")
    index = (index + k - 1) % len(curr_people)
