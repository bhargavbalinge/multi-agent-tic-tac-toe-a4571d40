def check_winner(board):
    # Existing logic to check for a winner
    pass

def is_board_full(board):
    # Existing logic to check if the board is full
    pass

def check_game_over(board):
    if check_winner(board):
        return "winner"
    elif is_board_full(board):
        return "draw"
    else:
        return "not_over"
