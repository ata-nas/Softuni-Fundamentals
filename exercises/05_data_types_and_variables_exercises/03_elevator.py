people = int(input())
capacity = int(input())

# courses = people // capacity
# remainder = people % capacity

courses, remainder = divmod(people, capacity)

if remainder != 0:
    courses += 1

print(courses)
