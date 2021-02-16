from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from Board import Board
from Mouse import Mouse

def treats_event(event, board: Board, mouse: Mouse) -> bool:
    """treats pygame events

            Parameters:
                    event (Event): pygame event
                    board (Board): scenery that contains the main grid

            Returns:
                    True (bool): quit game
                    False (bool): stay playing
    """
    if event.type == QUIT:
        return True
    elif event.type == MOUSEBUTTONUP:
        mouse.set_state(False)
    elif event.type == MOUSEBUTTONDOWN:
        mouse.set_state(True)
    return False
