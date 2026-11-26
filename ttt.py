"""
ttt.py
My version of tic-tac-toe game.
"""

'''
Represent the board
Display the board
Check whether a move is valid
Place a move on the board
Detect a winner
Detect a tie
Alternate turns in a game loop
Tie it together in main()
'''

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
        current_player, next_player = next_player, current_player



def create_empty_board():
    board = {}
    for coord in ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]:
        board[coord] = BLANK
    return board

def get_board_string(board):
    return f"""
     a   b   c
    ___ ___ ___
 1 | {board["1a"]} | {board["1b"]} | {board["1c"]} |
   +———+———+———+
 2 | {board["2a"]} | {board["2b"]} | {board["2c"]} |
   +———+———+———+
 3 | {board["3a"]} | {board["3b"]} | {board["3c"]} |
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

main()
