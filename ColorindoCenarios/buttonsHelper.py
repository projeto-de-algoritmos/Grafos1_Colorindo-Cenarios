from pygame import Surface
from Board import Board
from colors import STANDARD_COLOR, RED, GREEN, WALL, YELLOW, BLUE,PURPLE,PINK, GREY

def buttons_on_click(x: int, y: int, color: tuple, buttons: list) -> tuple:
    """check if the mouse click the button

            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
                    color (tuple): current color
                    buttons (list<Button>): lift of all buttons

            Returns:
                    Color of the current button or current color
    """
    for i in range(len(buttons)):
        if buttons[i].check(x,y):
            if(buttons[i].color == STANDARD_COLOR):
                return WALL
            else:
                return buttons[i].color
    return color

def draw_or_fill(x: int, y: int, board: Board, new_color: tuple) -> None:
    """Draw WALL or call flood fill

            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
                    board (Board): grid board
                    new_color (tuple): color of the floodfill function

            Returns:
                    None
    """
    if not board.out_of_range(x, y):
        if new_color == WALL:
            board.grid[x][y] = new_color
        elif new_color != GREY:
            board.flood_fill(x, y, board.grid[x][y], new_color)
    if new_color == GREY:
        for row in range(board.width):
            for column in range(board.height):
                board.grid[row][column] = STANDARD_COLOR

def draw_buttons(screen: Surface, buttons: list) -> None:
    """draw the buttons on the screen

            Parameters:
                    screen (Surface): current screen
                    buttons (list<Button>): lift of all buttons

            Returns:
                    Color of the current button
    """
    for i in range(len(buttons)):
        buttons[i].draw(screen, WALL)
