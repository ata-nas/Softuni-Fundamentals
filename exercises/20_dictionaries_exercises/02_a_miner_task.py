def get_minerals_dict():
    resutl_dict = {}

    while True:
        mineral = input()

        if mineral == 'stop':
            break

        quantity = int(input())

        resutl_dict[mineral] = resutl_dict.get(mineral, 0) + quantity

    return resutl_dict


def main():
    result = get_minerals_dict()

    [print(f'{key} -> {value}') for key, value in result.items()]


if __name__ == '__main__':
    main()
