"""
Tic Tac Toe Player
"""
import copy
import math

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
    if board == initial_state():
        return X

    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    if count % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Action Invalid")

    # make a copy of board
    results = copy.deepcopy(board)
    results[action[0]][action[1]] = player(board)
    return results


def check_winner(cell):
    if cell == X:
        return X
    elif cell == O:
        return O
    else:
        return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # row check
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return check_winner(board[i][0])

    # column check
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return check_winner(board[0][j])

    # diagonal check
    if board[0][0] == board[1][1] == board[2][2]:
        return check_winner(board[0][0])
    if board[2][0] == board[1][1] == board[0][2]:
        return check_winner(board[2][0])

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
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
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    val = float("-inf")
    move = None
    for action in actions(board):
        aux, act = min_value(result(board, action))
        if aux > val:
            val = aux
            move = action
            if val == 1:
                return val, move
    return val, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    val = float('inf')
    move = None
    for action in actions(board):
        aux, act = max_value(result(board, action))
        if aux < val:
            val = aux
            move = action
            if val == -1:
                return val, move
    return val, move
