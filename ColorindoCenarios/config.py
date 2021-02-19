import pygame
from colors import STANDARD_COLOR, RED, GREEN, WALL, BLACK
# Classes
from Mouse import Mouse
from Button import Button
from Board import Board

pygame.init()

screen_size = (1600,800)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK) # Set background color

# Screen title
pygame.display.set_caption("Colorindo Cenarios")

# Create an object to help track time
clock = pygame.time.Clock()

# All buttons
draw_button = Button(STANDARD_COLOR, 1095, 5, 460, 205, "DRAW")
red_button = Button(RED, 1095, 215, 225, 205, "RED")
green_button = Button(GREEN, 1330, 215, 225, 205, "GREEN")
buttons = [draw_button, green_button, red_button]

# Objects
board = Board(20, 20, 5, STANDARD_COLOR)
mouse = Mouse()

# Controls mouse color
new_color = WALL
