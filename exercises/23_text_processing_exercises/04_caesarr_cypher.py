user_input = input()

encrypted_text = ''

for char in user_input:
    encrypted_text += chr(ord(char) + 3)

print(encrypted_text)
