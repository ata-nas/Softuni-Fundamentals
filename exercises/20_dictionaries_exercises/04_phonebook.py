def generate_phonebook():
    result = {}

    while True:
        user_input = input()
        try:
            user_input = int(user_input)
            break
        except:
            command = user_input.split(sep="-")

            name = command[0]
            number = command[1]

            result[name] = number

    return result, user_input


def make_queries(phonebook_dict, queries):
    for _ in range(queries):
        query_name = input()

        try:
            number = phonebook_dict[query_name]
            print(f"{query_name} -> {number}")
        except:
            print(f'Contact {query_name} does not exist.')


def main():
    phonebook, queries_to_make = generate_phonebook()

    make_queries(phonebook, queries_to_make)


if __name__ == '__main__':
    main()
