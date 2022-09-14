def is_prime(n):
    for number in range(2, n):
        if n % number == 0:
            return False
    return True


user_input = int(input())

print(is_prime(user_input))
