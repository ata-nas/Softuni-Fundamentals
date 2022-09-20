people = [int(i) for i in input().split(sep=", ")]  # saves the input str in a list of ints
beggars = int(input())

output_list = []

for beggar_turn in range(beggars):
    sum_of_money = sum(people[index] for index in range(beggar_turn, len(people), beggars))
    output_list.append(sum_of_money)

print(output_list)

# another solution, more detailed for the sum() function
# people = [int(i) for i in input().split(sep=", ")]  # saves the input str in a list of ints
# beggars = int(input())
#
# output_list = []
#
# beggar_turn = 0
#
# while beggar_turn < beggars:
#     sum_of_money = 0
#     for index in range(beggar_turn, len(people), beggars):
#         sum_of_money += people[index]
#     output_list.append(sum_of_money)
#     beggar_turn += 1
#
# print(output_list)