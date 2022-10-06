def no_vowels(text: str):
    result_list = [letter for letter in text if letter.lower() not in ["a", "e", "i", "o", "u"]]
    return "".join(result_list)


user_input = input()

print(no_vowels(user_input))
