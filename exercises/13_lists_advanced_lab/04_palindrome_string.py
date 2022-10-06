def is_palindrome_word(word: str):
    return word[::-1] == word


user_input_words = input().split(sep=" ")
user_input_palindrome = input()

result_list = [item for item in user_input_words if is_palindrome_word(item)]

palindrome_count = result_list.count(user_input_palindrome)

print(f"{result_list}\n"
      f"Found palindrome {palindrome_count} times")
