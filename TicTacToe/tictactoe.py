"""
Tic Tac Toe Player
"""

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
    # Count number of X's and O's on the board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    # If X has more moves, it's O's turn, otherwise it's X's turn
    if x_count > o_count:
        return O
    else:
        return X


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
        raise Exception("Invalid action")
    
    # Create a deep copy of the board
    new_board = [row.copy() for row in board]
    
    # Apply the action to the new board
    i, j = action
    new_board[i][j] = player(board)
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal lines for winner
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != EMPTY:
        return board[2][0]
    
    # Check vertical lines for winner
    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != EMPTY:
        return board[0][2]
    
    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        # Winner - game is over
        return True

    # Check for tie
    for row in board:
        for cell in row:
            if cell == EMPTY:
                # Empty cell - not over
                return False
            
    # No winner and no empty cells - tie - game is over
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_move = None

    if current_player == X:
        best_value = -math.inf
        for move in actions(board):
            value = minimax_value(result(board, move))
            if value > best_value:
                best_value = value
                best_move = move
    else:
        best_value = math.inf
        for move in actions(board):
            value = minimax_value(result(board, move))
            if value < best_value:
                best_value = value
                best_move = move

    return best_move

def minimax_value(board):
    """
    Returns the minimax value of a board state.
    """
    if terminal(board):
        return utility(board)

    current_player = player(board)
    values = [minimax_value(result(board, move)) for move in actions(board)]

    if current_player == X:
        return max(values)
    return min(values)