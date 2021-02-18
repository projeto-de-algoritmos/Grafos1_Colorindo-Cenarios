# Libraries
import pygame
# Global constants and variables
from config import screen, clock, buttons, board, mouse, new_color
# Functions
from buttonsHelper import buttons_on_click, draw_or_fill, draw_buttons
from events import treats_event

done = False

while not done:
    board.draw_grid(screen)
    draw_buttons(screen, buttons)
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
        new_color = buttons_on_click(x, y, new_color, buttons)
        x, y = board.screen_to_grid(x, y)
        draw_or_fill(x, y, board, new_color)

