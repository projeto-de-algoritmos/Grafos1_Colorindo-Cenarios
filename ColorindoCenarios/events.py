from pygame import QUIT, MOUSEBUTTONDOWN, mouse
from colors import WALLS
from Board import Board

def treats_event(event, board: Board) -> bool:
    """treats pygame events

            Parameters:
                    event (Event): pygame event
                    board (Board): scenery that contains the main grid

            Returns:
                    bool
    """
    if event.type == QUIT:
        return False
    elif event.type == MOUSEBUTTONDOWN:
        pos = mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (board.width + board.margin)
        row = pos[1] // (board.height + board.margin)
        # Mark position with new color
        if not board.out_of_range(row, column):
            board.grid[row][column] = WALLS
    return True