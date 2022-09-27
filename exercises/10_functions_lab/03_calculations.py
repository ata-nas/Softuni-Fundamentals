ADD_OPERATOR = "add"
SUBTRACT_OPERATOR = "subtract"
MULTIPLY_OPERATOR = "multiply"
DIVIDE_OPERATOR = "divide"


def operation(first_num: int, second_num: int, operator: str):
    result = None
    if operator == ADD_OPERATOR:
        result = first_num + second_num
    elif operator == SUBTRACT_OPERATOR:
        result = first_num - second_num
    elif operator == MULTIPLY_OPERATOR:
        result = first_num * second_num
    elif operator == DIVIDE_OPERATOR:
        result = int(first_num / second_num)
    return result


command = input()
num_a = int(input())
num_b = int(input())

print(operation(num_a, num_b, command))
