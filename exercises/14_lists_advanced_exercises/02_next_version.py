def next_version(current_version: list):
    result = current_version
    result[2] += 1
    if result[2] == 10:
        result[2] = 0
        result[1] += 1
        if result[1] == 10:
            result[1] = 0
            result[0] += 1
    return [str(item) for item in result]


user_input_current_version = [int(ver) for ver in input().split(sep=".")]

result = ".".join(next_version(user_input_current_version))

print(result)
