"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            if board[i][j] == O:
                o += 1
    if o < x:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    # if new_board[action[0]][action[1]] != EMPTY:
    #     raise NameError("Action is invalide")
    if player(board) == X:
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O

    print("old:", board)
    print("new", new_board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][:3] == [X, X, X] or \
       board[1][0:3] == [X, X, X] or \
       board[2][0:3] == [X, X, X] or \
       board[0:3][0] == [X, X, X] or \
       board[0:3][1] == [X, X, X] or \
       board[0:3][2] == [X, X, X]:
        return X
    
    if board[0][0:3] == [O, O, O] or \
       board[1][0:3] == [O, O, O] or \
       board[2][0:3] == [O, O, O] or \
       board[0:3][0] == [O, O, O] or \
       board[0:3][1] == [O, O, O] or \
       board[0:3][2] == [O, O, O]:
        return O
    
    if board[0][0] == board[1][1] == board[2][2] == X or \
       board[2][0] == board[1][1] == board[0][2] == X:
        return X
    
    if board[0][0] == board[1][1] == board[2][2] == O or \
       board[2][0] == board[1][1] == board[0][2] == O:
        return O
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def minimax_helper(board):
    if terminal(board) == True:
        return utility(board)
    
    p = player(board)

    moves = actions(board)

    move_min = {-1, -1}
    move_zero = {-1, -1}
    move_max = {-1, -1}

    for move in moves:

        if minimax_helper(result(board, move)) == 1:
            move_max = move
        if minimax_helper(result(board, move)) == 0:
            move_zero = move
        if minimax_helper(result(board, move)) == -1:
            move_min = move    

    if p == X:
        if move_max != {-1, -1}:
            return move_max
        if move_zero != {-1, -1}:
            return move_zero
        return move_min
    else:
        if move_min != {-1, -1}:
            return move_min
        if move_zero != {-1, -1}:
            return move_zero
        return move_max

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    return minimax_helper(board)
    

