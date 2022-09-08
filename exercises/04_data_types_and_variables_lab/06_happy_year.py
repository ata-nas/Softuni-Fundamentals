user_year = int(input())

happy_year = False

while not happy_year:
    user_year += 1
    year_set = set()
    for i in range(len(str(user_year))):
        year_set.add(str(user_year)[i])
    if len(year_set) == len(str(user_year)):
        happy_year = True

print(user_year)
