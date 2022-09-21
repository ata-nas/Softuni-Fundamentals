index_sequence = input().split(sep=" ")
string_sequence = input()

index_search_sequence = []

for item in index_sequence:
    sum_current_index = sum(int(num) for num in item)  # same as a for loop
    index_search_sequence.append(sum_current_index)

result = ""

for index in index_search_sequence:
    curr_index = index
    while curr_index >= len(string_sequence):
        curr_index -= len(string_sequence)
    result += "".join(string_sequence[curr_index])
    string_sequence = string_sequence[:curr_index] + string_sequence[curr_index + 1:]

print(result)
