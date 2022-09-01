user_input = int(input())

number_of_messages = user_input

while number_of_messages > 0:
    number_of_messages -= 1
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command > 88:
        print("Bye.")
    else:
        print("GREAT!")
