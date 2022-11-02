def add_items_to_dict(add_items: list) -> dict:
    return {key: int(ord(key)) for key in add_items}


def main():
    user_input = input().split(sep=", ")

    result_dict = add_items_to_dict(user_input)

    print(result_dict)



if __name__ == '__main__':
    main()
