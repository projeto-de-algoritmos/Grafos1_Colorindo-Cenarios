from pygame import draw, Surface

class Board():
    def __init__(self, width: int, height: int, margin: int, standard_color: tuple) -> None:
        self.width = width
        self.height = height
        self.margin = margin
        self.color = standard_color
        # directions to walk
        self.dx = [ -1, 1, 0,  0]
        self.dy = [  0, 0, 1, -1]
        self.grid = [[standard_color for i in range(height)] for j in range(width)]

    def out_of_range(self, x: int, y: int) -> bool:
        """tells if x or y access self.grid invalid position

                Parameters:
                        x (int): x position in grid
                        y (int): y position in grid

                Returns:
                        bool
        """
        return (x < 0 or y < 0 or x >= self.width or y >= self.height)

    def change_grid_color(self, x: int, y: int, new_color: tuple) -> None:
        """change color after mouse click

                Parameters:
                        x (int): x screen coordinates
                        y (int): y screen coordinates

                Returns:
                        None
        """
        # Change the x/y screen coordinates to grid coordinates
        column = x // (self.width + self.margin)
        row = y // (self.height + self.margin)
        if not self.out_of_range(row, column):
            self.grid[row][column] = new_color
    
    def draw_grid(self, screen: Surface) -> None:
        """draw grid to specific screen

                Parameters:
                        screen (Surface): game screen

                Returns:
                        None
        """
        for row in range(self.width):
            for column in range(self.height):
                draw.rect(screen,
                          self.grid[row][column],
                          [(self.margin + self.width) * column + self.margin,
                          (self.margin + self.height) * row + self.margin,
                          self.width,
                          self.height])
    
    def flood_fill(self, x: int, y: int, color: tuple, new_color: tuple) -> None:
        """determines and alters the area connected to a given node in
        a multi-dimensional array based on a color matching attribute.

                Parameters:
                        x (int): x position in grid
                        y (int): y position in grid
                        color (str): current color
                        new_color (str): color to be drawn

                Returns:
                        None
        """
        if self.out_of_range(x, y) or self.grid[x][y] != color or color == new_color:
            return
   
        self.grid[x][y] = new_color
    
        for i in range(0, 4):
            self.flood_fill(x+self.dx[i], y+self.dy[i], color, new_color)

