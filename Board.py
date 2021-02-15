import colors

class Board():
    def __init__(self, width: int, height: int, margin: int) -> None:
        self.width = width
        self.height = height
        self.margin = margin
        self.color = COLOR
        # directions to walk
        self.dx = [ -1, 1, 0,  0]
        self.dy = [  0, 0, 1, -1]
        self.grid = [[COLOR for i in range(height)]] * width
    
    def flood_fill(x:int, y:int, color:str, new_color:str) -> None:
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
        if (x < 0 or y < 0 or x >= self.width or y >= self.height) or \
           (self.grid[x][y] != color):
            return
   
        self.grid[x][y] = new_color
    
        for i in range(0, 4):
            flood_fill(x+self.dx[i], y+self.dy[i], color, new_color)