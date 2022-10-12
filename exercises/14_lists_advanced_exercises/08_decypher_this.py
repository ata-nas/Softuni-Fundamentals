def decipher(user_str: str) -> str:
    """
    Deciphers code.
    :param user_str str
    :return: str
    """
    words = user_str.split(sep=" ")
    result = []
    for word in words:
        number = ""
        for char in word:
            if char.isdigit():
                number += char
                continue
            break
        word_second_half = word[len(number):]
        if len(word_second_half) > 1:
            res_word = chr(int(number)) + word_second_half[-1] + word_second_half[1:-1] + word_second_half[0]
        else:
            res_word = chr(int(number)) + word_second_half
        result.append(res_word)
    return " ".join(result)


user_input = input()
print(decipher(user_input))
