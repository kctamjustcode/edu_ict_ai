import math, time, random, copy

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
    for i in range(size):
        for j in range(size):
            if bord[i][j] == '-':
                cnt += 1
    return cnt

def check_terminating(board):
    for a in range(1, size-1):
        for b in range(1, size-1):
            board_window = [[ttt_board[a-1][b-1],ttt_board[a-1][b],ttt_board[a-1][b+1]],[ttt_board[a][b-1], ttt_board[a][b], ttt_board[a][b+1]],[ttt_board[a+1][b-1],ttt_board[a+1][b],ttt_board[a+1][b+1]]]
            #print(board_window)
            checking_board = check_winning(board_window)
            if checking_board != 0:
                return checking_board
    return 0


def get_available_indice(board):
    moves = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == '-':
                moves.append((i,j))
    return moves


size = 4
game_length = size**2
status = [dict() for _ in range(game_length)]
freq = [dict() for _ in range(game_length)]

t1 = time.time()
for _ in range(1000000):
    ttt_board = [[ '-' for _ in range(size)] for _ in range(size)]
    player_one_round = True
    cnt = 0
    hist = []

    while check_terminating(ttt_board) == 0:
        plyr_moves = get_available_indice(ttt_board)
        if len(plyr_moves) != 0:
            move = plyr_moves[random.randint(0, len(plyr_moves)-1)]     # to be changed to for loop based on dp
        else:
            break

        if player_one_round:
            ttt_board[move[0]][move[1]] = 1
            player_one_round = False
        else:
            ttt_board[move[0]][move[1]] = -1
            player_one_round = True

        
        if str(ttt_board) not in freq[cnt].keys():
            freq[cnt][str(ttt_board)] = 1     # modify to MC Tree Search, on value part
        else:
            freq[cnt][str(ttt_board)] += 1
        

        hist.append(str(ttt_board))
        terminating_result = check_terminating(ttt_board)
        if terminating_result != 0:
            for i in range(len(hist)):
                if hist[i] not in status[i].keys():
                    status[i][hist[i]] = terminating_result     # adjusting scores
                else:
                    status[i][hist[i]] += terminating_result    # adjusting scores

        cnt += 1
t2 = time.time()
    
print('initial status: ',status[0])
print('---')
print('final status: ', status[-1])
'''
for key in status[-2].keys():
    if status[-2][key] < 0:
        #print(key)
        pass
'''
print("initial freq cnt: ",freq[0])
print('---')
print("final freq cnt: ", freq[-1])
'''
for key in freq[-2].keys():
    if freq[-2][key] < 0:
        #print(key)
        pass
'''
print(t2-t1)

# print(check_winning([[1, 1, 1], [1, -1, -1], [1, -1, -1]]))

'''
#restoring key to list
a = str([[1, 1, -1], [1, -1, -1], [1, -1, 1]])
import ast
result = ast.literal_eval(a)
print(result)
'''

'''
# sorting dictionary values
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)  # Output: {'c': 3, 'b': 2, 'a': 1}
'''

'''
# for loop returning remark
def check_forloop():
    for i in range(3):
        for j in range(3):
            return (i,j)

>>>check_forloop()
Output:
>>>(0, 0)
'''