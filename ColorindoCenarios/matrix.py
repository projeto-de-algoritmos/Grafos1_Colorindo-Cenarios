from flask import render_template

class Scenery():
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        # directions to walk
        self.dx = [ -1, 1, 0,  0]
        self.dy = [  0, 0, 1, -1]
        self.canvas = [["white" for i in range(columns)]] * rows
    
    def flood_fill(x:int, y:int, color:str, new_color:str) -> None:
        """determines and alters the area connected to a given node in
        a multi-dimensional array based on a color matching attribute.

                Parameters:
                        x (int): x position in canvas
                        y (int): y position in canvas
                        color (str): current color
                        new_color (str): color to be drawn

                Returns:
                        None
        """
        if (x < 0 or y < 0 or x >= self.rows or y >= self.columns) or \
           (self.canvas[x][y] != color):
            return
   
        self.canvas[x][y] = new_color
    
        for i in range(0, 4):
            flood_fill(x+self.dx[i], y+self.dy[i], color, new_color)

def matrix(rows=30, columns=40):
    drawable_scenery = Scenery(rows, columns)
    return drawable_scenery.canvas