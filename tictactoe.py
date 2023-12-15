"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

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
    if new_board[action[0]][action[1]] != EMPTY:
        raise NameError("Action is invalide")
    if player(board) == X:
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O
    return new_board


def row_and_col_check(np_board, player):
    win_state = np.array([player, player, player])
    if (np_board[0, :] == win_state).all() or \
       (np_board[1, :] == win_state).all() or \
       (np_board[2, :] == win_state).all() or \
       (np_board[:, 0] == win_state).all() or \
       (np_board[:, 1] == win_state).all() or \
       (np_board[:, 2] == win_state).all():
        return player
    return None


def diag_check(np_board, player):
    if np_board[0][0] == np_board[1][1] == np_board[2][2] == player or \
       np_board[2][0] == np_board[1][1] == np_board[0][2] == player:
        return player
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    np_board = np.array(board)

    if row_and_col_check(np_board, X) != None or \
        diag_check(np_board, X) != None:
        return X
    if row_and_col_check(np_board, O) != None or \
        diag_check(np_board, O) != None:
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
    """
    returns [best_score, optimal_action]
    """
    if terminal(board) == True:
        return [utility(board), (-1, -1)]
    
    p = player(board)
    moves = actions(board)
    best_move = (-1, -1)
    maximum = -2
    minimum = 2

    for move in moves:
        new_board = result(board, move)
        if p == X:
            if minimax_helper(new_board)[0] > maximum:
                maximum = minimax_helper(new_board)[0]
                best_move = move
        else:
            if minimax_helper(new_board)[0] < minimum:
                minimum = minimax_helper(new_board)[0]
                best_move = move
    
    if p == X:
        return [maximum, best_move]
    return [minimum, best_move]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    return minimax_helper(board)[1]
    

