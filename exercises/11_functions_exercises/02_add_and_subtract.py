def sum_numbers(x: int, y: int):
    return x + y


def subtract(w: int, z: int):
    return w - z


def add_and_subtract(a: int, b: int, c: int):
    sum_nums = sum_numbers(a, b)
    return subtract(sum_nums, c)


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
