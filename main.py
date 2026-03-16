def is_draw(board):
    # Check if the board is full
    if all(cell != ' ' for cell in board):
        return True
    return False