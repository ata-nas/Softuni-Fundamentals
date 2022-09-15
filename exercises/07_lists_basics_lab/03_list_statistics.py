amount_of_numbers = int(input())

positives = []
negatives = []

for _ in range(amount_of_numbers):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(f"{positives}\n"
      f"{negatives}\n"
      f"Count of positives: {len(positives)}\n"
      f"Sum of negatives: {sum(negatives)}")
