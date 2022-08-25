total_patterns = int(input())

for star in range(total_patterns):
    for _ in range(star + 1):
        print("*", end="")
    print()

for star in range(total_patterns - 1, 0, -1):
    for _ in range(star):
        print("*", end="")
    print()
