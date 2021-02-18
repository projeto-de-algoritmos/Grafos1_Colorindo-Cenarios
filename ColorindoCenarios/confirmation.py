from pygame import Surface
from Button import Button
from Board import Board
from colors import STANDARD_COLOR, WALL, RED, GREEN

# Buttons
draw_button = Button(STANDARD_COLOR,1095,5,460,205,"DRAW")
red_button = Button(RED,1095,215,225,205,"RED")
green_button = Button(GREEN,1330,215,225,205,"GREEN")

all_buttons = [draw_button, green_button, red_button]

def confirmation_button(x: int, y: int, color: tuple)-> tuple:
    """check if the mouse click the button

            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
                    color (tuple): current color
                    draw_button (Button): button to select draw
                    green_button (Button): button for green
                    red_button (Button): button for red

            Returns:
                    Color of the current button or the current color
    """
    for i in range(len(all_buttons)):
        if all_buttons[i].check(x,y):
            if(all_buttons[i].color == STANDARD_COLOR):
                return WALL
            else:
                return all_buttons[i].color
    return color

def confirmation_fill(x: int, y: int, board: Board, new_color: tuple) -> None:
    """check the current draw methot

            Parameters:
                    x (int): x screen coordinate
                    y (int): y screen coordinate
                    board (Board): grid board
                    new_color (tuple): color of the floodfill function

            Returns:
                    None
    """
    if not board.out_of_range(x,y):
            if new_color == WALL:
                board.grid[x][y] = WALL
            else:
                board.flood_fill(x, y, board.grid[x][y],new_color)

def confirmation_draw_button(screen: Surface) -> None:
    """draw the buttons on the screen

            Parameters:
                    screen (Surface): current screen
                    draw_button (Button): button to select draw
                    green_button (Button): button for green
                    red_button (Button): button for red


            Returns:
                    Color of the current button
    """
    for i in range(len(all_buttons)):
        all_buttons[i].draw(screen,WALL)
