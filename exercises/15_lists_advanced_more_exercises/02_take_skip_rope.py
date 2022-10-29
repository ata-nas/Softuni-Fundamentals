def decoding_algorithm(encoded_string: str):
    decoded_string = ''

    numbers_list = [int(num) for num in encoded_string if num.isdigit()]
    non_numbers_string = "".join([item for item in encoded_string if not item.isdigit()])

    takes_list = [int(num) for index, num in enumerate(numbers_list) if index % 2 == 0]
    skips_list = [int(num) for index, num in enumerate(numbers_list) if index % 2 != 0]

    while non_numbers_string:
        if not takes_list or not skips_list:
            break

        for index in range(takes_list[0]):
            if not non_numbers_string:
                break
            decoded_string += non_numbers_string[0]
            non_numbers_string = non_numbers_string[1:]

        takes_list.pop(0)

        for index in range(skips_list[0]):
            if not non_numbers_string:
                break
            non_numbers_string = non_numbers_string[1:]

        skips_list.pop(0)

    return decoded_string


user_input_string = input()

print(decoding_algorithm(user_input_string))
