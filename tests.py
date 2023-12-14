import tictactoe as ttt

EMPTY = None

board1 = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

board2 = [["X", EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board3 = [["X", "O", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board4 = [["X", "O", "X"],
            ["O", "O", "X"],
            [EMPTY, "X", EMPTY]]

board5 = [["X", "O", "X"],
            ["X", "O", "X"],
            ["O", "O", EMPTY]]

board6 = [["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "O", "X"]]

board7 = [["O", "X", "O"],
            ["X", "O", "X"],
            ["X", "X", "O"]]

board8 = [["X", "O", "O"],
            ["X", "O", "X"],
            ["O", "X", "X"]]

board9 = [["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]]

def test_player():

    print(ttt.player(board1), "should be equal X")
    print(ttt.player(board2), "should be equal O")
    print(ttt.player(board3), "should be equal X")
    print(ttt.player(board4), "should be equal O")
    print(ttt.player(board5), "should be equal X")

def test_actions():
    print(ttt.actions(board1))
    print(ttt.actions(board2))
    print(ttt.actions(board3))
    print(ttt.actions(board4))
    print(ttt.actions(board5))

def test_result():
    print(ttt.result(board1, (1, 2)))
    print(ttt.result(board2, (2, 2)))
    print(ttt.result(board5, (0, 0)))


def test_winner():
    print(ttt.winner(board1))
    print(ttt.winner(board5))
    print(ttt.winner(board6))
    print(ttt.winner(board7))
    print(ttt.winner(board8))
    print(ttt.winner(board9))

def test_terminal():
    print(ttt.terminal(board1))
    print(ttt.terminal(board2))
    print(ttt.terminal(board3))
    print(ttt.terminal(board4))
    print(ttt.terminal(board5))
    print(ttt.terminal(board9))

def test_utility():
    print(ttt.utility(board1))
    print(ttt.utility(board2))
    print(ttt.utility(board3))
    print(ttt.utility(board4))
    print(ttt.utility(board5))
    print(ttt.utility(board6))
    print(ttt.utility(board7))
    print(ttt.utility(board8))
    print(ttt.utility(board9))

def test_minimax():
    # print(ttt.minimax(board1))
    # print(ttt.minimax(board2))
    # print(ttt.minimax(board3))
    print(ttt.minimax(board4))
    print(ttt.minimax(board5))
    print(ttt.minimax(board6))
    print(ttt.minimax(board7))
    print(ttt.minimax(board8))
    print(ttt.minimax(board9))


# test_player()
# test_actions()
# test_result()
# test_winner()
# test_terminal()
# test_utility()
test_minimax()