def synonym_dict(inputs: int) -> dict:
    result_dict = {}

    for _ in range(inputs):
        key = input()
        value = input()

        if key not in result_dict.keys():
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)

    return result_dict


def print_synonyms(syn_dict: dict) -> list:
    for key, items in syn_dict.items():
        print(f"{key} - {', '.join(items)}")


def main():
    user_input_iterations = int(input())

    synonyms_dict = synonym_dict(user_input_iterations)

    result = print_synonyms(synonyms_dict)


if __name__ == '__main__':
    main()
