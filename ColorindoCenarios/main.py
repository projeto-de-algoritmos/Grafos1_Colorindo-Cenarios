# Libraries
import pygame
# Global constants and variables
from config import screen, clock
from colors import STANDARD_COLOR, WALL
# Functions
from events import treats_event
# Classes
from Board import Board
from Mouse import Mouse

board = Board(30, 30, 5, STANDARD_COLOR)
mouse = Mouse()
done = False

while not done:
    # Draw the grid
    board.draw_grid(screen)
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
        board.change_grid_color(x, y, WALL)
