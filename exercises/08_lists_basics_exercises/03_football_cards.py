card_sequence = input().split()

team_a = list(range(1, 11 + 1))
team_b = list(range(1, 11 + 1))

game_terminated = False

for card in card_sequence:
    current_card = card.split(sep="-")
    if "A" in current_card and int(current_card[1]) in team_a:
        team_a.remove(int(current_card[1]))
    elif "B" in current_card and int(current_card[1]) in team_b:
        team_b.remove(int(current_card[1]))
    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break

if game_terminated:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}\n"
          f"Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
