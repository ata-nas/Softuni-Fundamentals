first_word, second_word = input().split(sep=' ')

if len(first_word) >= len(second_word):
    longest_word = first_word
    shortest_word = second_word
else:
    longest_word, shortest_word = second_word, first_word

total_sum = 0

for index in range(len(shortest_word)):
    total_sum += ord(longest_word[index]) * ord(shortest_word[index])

if len(longest_word) != len(shortest_word):
    additional_word = longest_word[len(shortest_word):]
    for index in range(len(longest_word[len(shortest_word)])):
        total_sum += ord(additional_word[index])

print(total_sum)
