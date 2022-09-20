cards = input().split()
shuffles = int(input())

final_deck = cards

for _ in range(shuffles):
    current_deck = []
    first_half = list(final_deck[:len(cards) // 2])
    second_half = list(final_deck[len(cards) // 2:])
    for index in range(len(first_half)):
        # current_deck.append(first_half[index])
        # current_deck.append(second_half[index])
        current_deck.extend((first_half[index], second_half[index]))
    final_deck = current_deck

print(final_deck)
