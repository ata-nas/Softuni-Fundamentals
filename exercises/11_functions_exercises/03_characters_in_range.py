def ascii_in_range(first_char: str, second_char: str):
    list_user = [chr(char) for char in range(ord(first_char) + 1, ord(second_char))]
    return " ".join(list_user)


first_char = input()
second_char = input()

print(ascii_in_range(first_char, second_char))
