first_int = int(input())
second_int = int(input())

print(f"Before:\n"
      f"a = {first_int}\n"
      f"b = {second_int}")

first_int, second_int = second_int, first_int  # Tuple assignment

# temp = first_int
# first_int = second_int
# second_int = temp

print(f"After:\n"
      f"a = {first_int}\n"
      f"b = {second_int}")
