key = int(input())
lines = int(input())

result = ""
for _ in range(lines):
    user_input = input()
    real_word = ord(user_input) + key
    result = result + "".join(chr(real_word))

print(result)
