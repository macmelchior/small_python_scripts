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

# Grid coordinates, 1 is top left, 9 is bottom right
COORDINATES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = "✕"
O = "○"
BLANK = " "

def main():
    board = create_empty_board(COORDINATES)
    current_player, next_player = X, O
    print(get_board_string(board))

    while True:
        move = get_player_move(current_player, board)
        place_player_move(current_player, board, move)
        print(get_board_string(board))
        current_player, next_player = next_player, current_player



def create_empty_board(coordinates):
    board = {}
    for coord in coordinates:
        board[coord] = BLANK
    return board

def get_board_string(board):
    return f"""
+-----------+
| {board[1]} | {board[2]} | {board[3]} |
+---+---+---+
| {board[4]} | {board[5]} | {board[6]} |
+---+---+---+
| {board[7]} | {board[8]} | {board[9]} |
+-----------+
"""

def get_player_move(player, board):
    valid = False
    while not valid:
        move = int(input(f"What will {player} do? (1-9)"))
        if move in COORDINATES and board[move] == " ":
            valid = True
    return move

def place_player_move(player, board, move):
    board[move] = player

main()
