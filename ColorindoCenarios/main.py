# Libraries
import pygame
# Global constants and variables
from config import screen, clock
from colors import STANDARD_COLOR
# Functions
from events import treats_event
# Classes
from Board import Board

board = Board(30, 30, 5, STANDARD_COLOR)
done = False

while not done:
    # Draw the grid
    board.draw(screen)
    # Frame rate
    clock.tick(60)
    # Update screen
    pygame.display.flip()
    # Treats player interaction
    for event in pygame.event.get():
        done = treats_event(event, board)
