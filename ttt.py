"""
ttt.py
My version of tic-tac-toe game.
"""

X = "X"
O = "O"
BLANK = " "

def main():
    board = create_empty_board()
    current_player, next_player = X, O
    print(get_board_string(board))

    while True:
        move = get_player_move(current_player, board)
        place_player_move(current_player, board, move)
        print(get_board_string(board))
        if check_win(board, current_player):
            print(f"Player {current_player} won!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        current_player, next_player = next_player, current_player



def create_empty_board():
    board = {}
    for coord in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]:
        board[coord] = BLANK
    return board

def get_board_string(board):
    return f"""
     1   2   3
    ___ ___ ___
 a | {board["a1"]} | {board["a2"]} | {board["a3"]} |
   +———+———+———+
 b | {board["b1"]} | {board["b2"]} | {board["b3"]} |
   +———+———+———+
 c | {board["c1"]} | {board["c2"]} | {board["c3"]} |
    ‾‾‾ ‾‾‾ ‾‾‾
"""

def get_player_move(player, board):
    valid = False
    while not valid:
        move = input(f"What will {player} do? (1-9) ")
        if move in board.keys() and board[move] == " ":
            valid = True
    return move

def place_player_move(player, board, move):
    board[move] = player

def check_win(board, player):
    win = False
    """
    1. Combinations of keys which give horizontal, vertical, and diagonals.
    2. Check if there are three X's or O's in a row, diagonally, or vertically.
    """
    combinations = {
        "horizontal_top": [board["a1"], board["a2"], board["a3"]],
        "horizontal_middle": [board["b1"], board["b2"], board["b3"]],
        "horizontal_bottom": [board["c1"], board["c2"], board["c3"]],
        "vertical_left": [board["a1"], board["b1"], board["c1"]],
        "vertical_middle": [board["a2"], board["b2"], board["c2"]],
        "vertical_right": [board["a3"], board["b3"], board["c3"]],
        "diagonal_1" : [board["a1"], board["b2"], board["c3"]],
        "diagonal_2" : [board["a3"], board["b2"], board["c1"]]
        }
    for combination in combinations.values():
        if combination == [player, player, player]:
            win = True
    return win

def check_draw(board):
    count = 0
    for field in board.values():
        if field != " ":
            count += 1
    return count == 9

main()
