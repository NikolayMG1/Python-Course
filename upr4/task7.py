def determine_winner(board):
    def check_winner(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    if check_winner('X'):
        return 'X'
    elif check_winner('O'):
        return 'O'
    else:
        return 'Draw'

# Test cases
board_1 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]
board_2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['O', 'X', 'X']
]
board_3 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]
board_4 = [
    ['X', 'X', 'X'],
    ['O', 'O', None],
    [None, None, None]
]
board_5 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'X'],
    ['O', 'O', 'O']
]
board_6 = [
    ['O', 'O', 'X'],
    ['O', 'X', None],
    ['X', 'X', None]
]
board_7 = [
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['X', 'X', 'O']
]
board_8 = [
    ['O', 'X', 'O'],
    ['O', 'X', None],
    ['X', 'X', None]
]
board_9 = [
    ['X', 'X', 'O'],
    [None, 'X', 'O'],
    [None, None, 'O']
]

assert determine_winner(board_1) == 'X'
assert determine_winner(board_2) == 'O'
assert determine_winner(board_3) == 'Draw'
assert determine_winner(board_4) == 'X'
assert determine_winner(board_5) == 'O'
assert determine_winner(board_6) == 'X'
assert determine_winner(board_7) == 'X'
assert determine_winner(board_8) == 'X'
assert determine_winner(board_9) == 'O'
