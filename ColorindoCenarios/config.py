import pygame
from colors import STANDARD_COLOR, RED, GREEN, WALL, BLACK, BLUE, YELLOW, PURPLE, PINK, GREY, GOLD, BROWN
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
draw_button = Button(STANDARD_COLOR, 815, 5, 225, 400, "DRAW")
clear_button = Button(GREY, 815, 410, 225, 400, "CLEAR")

gold_button = Button(GOLD, 1095, 5, 225, 200, "GOLD")
brown_button = Button(BROWN, 1330, 5, 225, 200, "BROWN")
red_button = Button(RED, 1095, 210, 225, 200, "RED")
green_button = Button(GREEN, 1330, 210, 225, 200, "GREEN")
yellow_button = Button(YELLOW, 1095, 410, 225, 200, "YELLOW")
blue_button = Button(BLUE, 1330, 410, 225, 200, "BLUE")
purple_button = Button(PURPLE, 1095, 610, 225, 200, "PURPLE")
pink_button = Button(PINK, 1330, 610, 225, 200, "PINK")
buttons = [draw_button, clear_button, brown_button, gold_button, green_button, red_button, yellow_button, blue_button,purple_button,pink_button]

# Objects
board = Board(25, 25, 5, STANDARD_COLOR)
mouse = Mouse()

# Controls mouse color
new_color = WALL
