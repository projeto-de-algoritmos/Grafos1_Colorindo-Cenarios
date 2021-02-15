import pygame
import colors
import Board

#MENU
MENU = 0

#Init pygame
pygame.init()

#Creating screen
size = (1600,800)
screen = pygame.display.set_mode(size)

# Set the screen background
screen.fill(BLACK)

#Loop until close
done = False

#Title and icon
pygame.display.set_caption("Colorindo Cenarios")

#Clock
clock = pygame.time.Clock()



# -------- Main Loop -----------
while not done:
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and MENU == 0:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = BLACK
            print("Click ", pos, "Grid coordinates: ", row, column)
    

    

    # Draw the grid
    for row in range(30):
        for column in range(30):
            pygame.draw.rect(screen,
                             grid[row][column],
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    #Frame rate
    clock.tick(60)
 
    #Update screen
    pygame.display.flip()
 
#Quit
pygame.quit()