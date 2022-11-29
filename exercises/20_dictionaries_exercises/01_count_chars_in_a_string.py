def count_chars(input_text: str) -> list:
    result_dict = {}

    for char in input_text:
        if char == " ":
            continue

        if char not in result_dict.keys():
            result_dict[char] = 1
        else:
            result_dict[char] += 1

    return [f"{key} -> {values}" for key, values in result_dict.items()]


def main():
    user_input = input()

    result = count_chars(user_input)

    print(*result, sep="\n")


if __name__ == '__main__':
    main()
