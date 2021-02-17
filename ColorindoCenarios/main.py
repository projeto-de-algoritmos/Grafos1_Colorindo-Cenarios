# Libraries
import pygame
# Global constants and variables
from config import screen, clock
from colors import STANDARD_COLOR, WALL, RED, GREEN
from confirmation import draw_button,red_button,green_button
# Functions
from confirmation import confirmation_button, confirmation_fill, confirmation_draw_button
from events import treats_event
# Classes
from Board import Board
from Mouse import Mouse
from Button import Button

new_color = WALL

board = Board(30, 30, 5, STANDARD_COLOR)
mouse = Mouse()
done = False

while not done:
    # Draw the grid
    board.draw_grid(screen)
    # Draw the buttons
    confirmation_draw_button(screen, draw_button, green_button, red_button)
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
        new_color = confirmation_button(x, y, new_color, draw_button, green_button, red_button)
        # Grid change
        x, y = board.screen_to_grid(x,y)
        #Draw/Flood
        confirmation_fill(x, y, board, new_color)