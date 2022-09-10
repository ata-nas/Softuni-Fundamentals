ascii_start = int(input())
ascii_end = int(input())

for char in range(ascii_start, ascii_end + 1):
    current_char = chr(char)
    print(current_char, end=" ")
