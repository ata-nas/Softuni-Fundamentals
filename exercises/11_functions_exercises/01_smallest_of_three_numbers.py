def smallest_of_three(x: int, y: int, z: int):
    return min([x, y, z])


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_of_three(first_num, second_num, third_num))
