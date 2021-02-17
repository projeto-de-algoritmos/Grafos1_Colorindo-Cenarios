# Libraries
import pygame
# Global constants and variables
from config import screen, clock
from colors import STANDARD_COLOR, WALL, RED, GREEN
# Functions
from events import treats_event
# Classes
from Board import Board
from Mouse import Mouse
from Button import Button

new_color = WALL

board = Board(30, 30, 5, STANDARD_COLOR)
mouse = Mouse()
done = False
# Buttons
draw_button = Button(STANDARD_COLOR,1095,5,460,205,"DRAW")
red_button = Button(RED,1095,215,225,205,"RED")
green_button = Button(GREEN,1330,215,225,205,"GREEN")

while not done:
    # Draw the grid
    board.draw_grid(screen)
    # Draw the buttons
    draw_button.draw(screen,WALL)
    red_button.draw(screen,WALL)
    green_button.draw(screen,WALL)
    # Frame rate
    clock.tick(60)
    # Update screen
    pygame.display.flip()
    # Treats player interaction
    for event in pygame.event.get():
        done = treats_event(event, board, mouse)
    # If mouse is pressed then change color
    if mouse.state:
        x, y = pygame.mouse.get_pos()
        # Buttons
        if draw_button.check(x,y):
            new_color = WALL
        elif green_button.check(x,y):
            new_color = GREEN
        elif red_button.check(x,y):
            new_color = RED   
        # Grid change
        x, y = board.screen_to_grid(x,y)

        #Draw/Flood
        #board.change_grid_color(x, y, new_color)
        if not board.out_of_range(x,y):
            if new_color == WALL:
                board.grid[x][y] = WALL
            else:
                board.flood_fill(x, y, board.grid[x][y],new_color)
