class Board:
    def __init__(self, board_arrangement):
        self.board_arrangement = board_arrangement
        self.score = 0


class Move:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def make_move(self, coordinates):
        pass


def play():
    user_input_rows_in_field = int(input())

    user_input_board = [[int(position) for position in input().split(sep=' ')] for row in
                        range(user_input_rows_in_field)]

    user_input_moves = [tuple(int(pos) for pos in move.split(sep="-")) for move in input().split(sep=" ")]

    b = Board(user_input_board)

    for row, col in user_input_moves:
        if b.board_arrangement[row][col] == 0:
            continue

        b.board_arrangement[row][col] -= 1
        if b.board_arrangement[row][col] == 0:
            b.score += 1

    return b.score


def main():
    print(play())


if __name__ == '__main__':
    main()