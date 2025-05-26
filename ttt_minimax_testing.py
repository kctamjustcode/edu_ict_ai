import math

ttt_board = [[ '-' for _ in range(3)] for _ in range(3)]

# existence of winning moves
# counting of available spaces
# scoring

# Assuming the first player is maximizer, second player is minimizer.

def check_winning(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and type(board[i][0]) == int:
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and type(board[0][i]) == int:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and type(board[1][1]) == int:
        return board[1][1]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and type(board[1][1]) == int:
        return board[1][1]
    return 0

def count_remaining(bord):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if bord[i][j] == '-':
                cnt += 1
    return cnt

import copy

def minimax(bord, maxminPlayer):
    if check_winning(bord) != 0:
        return check_winning(bord)
    elif count_remaining(bord) == 0:
        return 0
    #print(bord, maxminPlayer)
    if maxminPlayer:
        val = -2
        for i in range(3):
            for j in range(3):
                if bord[i][j] == '-':
                    bord_cp = copy.deepcopy(bord)
                    bord_cp[i][j] = 1
                    val = max(val, minimax(bord_cp, False))
        return val
    else:
        val = +2
        for i in range(3):
            for j in range(3):
                if bord[i][j] == '-':
                    bord_cp = copy.deepcopy(bord)
                    bord_cp[i][j] = -1
                    val = min(val, minimax(bord_cp, True))
        return val

print(minimax(ttt_board, True))

