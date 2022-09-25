first_line = input()
second_line = input()
third_line = input()

game_board = list(first_line.split(sep=" ")) + list(second_line.split(sep=" ")) + list(third_line.split(sep=" "))

first_player_won = (
        (game_board[0] == "1" and game_board[1] == "1" and game_board[2] == "1")
     or (game_board[3] == "1" and game_board[4] == "1" and game_board[5] == "1")
     or (game_board[6] == "1" and game_board[7] == "1" and game_board[8] == "1")
     or (game_board[0] == "1" and game_board[3] == "1" and game_board[6] == "1")
     or (game_board[1] == "1" and game_board[4] == "1" and game_board[7] == "1")
     or (game_board[2] == "1" and game_board[5] == "1" and game_board[8] == "1")
     or (game_board[0] == "1" and game_board[4] == "1" and game_board[8] == "1")
     or (game_board[2] == "1" and game_board[4] == "1" and game_board[6] == "1")
)

second_player_won = (
        (game_board[0] == "2" and game_board[1] == "2" and game_board[2] == "2")
     or (game_board[3] == "2" and game_board[4] == "2" and game_board[5] == "2")
     or (game_board[6] == "2" and game_board[7] == "2" and game_board[8] == "2")
     or (game_board[0] == "2" and game_board[3] == "2" and game_board[6] == "2")
     or (game_board[1] == "2" and game_board[4] == "2" and game_board[7] == "2")
     or (game_board[2] == "2" and game_board[5] == "2" and game_board[8] == "2")
     or (game_board[0] == "2" and game_board[4] == "2" and game_board[8] == "2")
     or (game_board[2] == "2" and game_board[4] == "2" and game_board[6] == "2")
)

if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")
