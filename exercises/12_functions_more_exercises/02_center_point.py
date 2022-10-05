from math import floor


def closest_distance(x1, y1, x2, y2):
    return (floor(x1), floor(y1)) if (abs(x1) + abs(y1)) <= (abs(x2) + abs(y2)) else (floor(x2), floor(y2))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_distance(x1, y1, x2, y2))
