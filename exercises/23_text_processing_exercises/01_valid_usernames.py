import string

usernames = input().split(sep=', ')

for username in usernames:
    if 3 <= len(username) <= 16:
        for char in username:
            if char not in '-_' + string.digits + string.ascii_letters:
                break
        else:
            print(username)
