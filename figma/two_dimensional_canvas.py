# On a 2d canvas, implement three methods paint(x, y, color),
# undo(), redo() and read(x,y)‍‍‍‍‍‍‌‌‌‌‌‍‌‍‍‌‌‍‍, read(x, y) will return the color of [x, y]
# width = x
# height = y

class Canvas2D:
    def __init__(self, width, height, color="blue"):
        self.width = width
        self.height = height
        self.grid = []
        
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(color)
            self.grid.append(row)
            
        self.undo_stack = []
        self.redo_stack = []
    
    
    def paint(self, x, y, color):
        # apply color to the grid
        
        if not self._is_within_bounds(x, y):
            print(f"Coordinates {x} and {y} are out of bounds")
            return

        old_grid_color = self.grid[y][x]
        # store this old grid color in undo stack
        
        if old_grid_color != color:
            self.undo_stack.append((x, y, old_grid_color, color))
            self.redo_stack.clear()
        
        self.grid[y][x] = color

    def read(self, x, y):
        if not self._is_within_bounds(x, y):
            print(f"Cannot read color of grid {x}, {y}, out of bounds")
            return
        grid_color = self.grid[y][x]
        
        return grid_color
    
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        
        x, y, old_color, new_color = self.undo_stack.pop()
        
        self.grid[y][x] = old_color
        self.redo_stack.append((x, y, new_color, old_color))
        print("undo", self.undo_stack)
        
        
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        
        x, y, new_color, old_color = self.redo_stack[-1]
        self.grid[y][x] = new_color
        self.undo_stack.append((x, y, old_color, new_color))
        self.redo_stack.pop()
        print("redo", self.redo_stack)
        
    def _is_within_bounds(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("out of bounds", self.width, x, y, self.height)
            return False
        return True
    
    def print_grid(self):
        """Print the current state of the canvas grid"""
        print("Canvas Grid:")
        for row in self.grid:
            print(row)
    



c2d = Canvas2D(6, 10, "red")
c2d.paint(3, 7, "purple")
c2d.print_grid()
c2d.paint(2, 6, "green")
c2d.print_grid()
c2d.paint(4, 9, "blue")
c2d.print_grid()
c2d.undo()
c2d.undo()
c2d.redo()
print("wat", c2d.read(1, 6,))
c2d.redo()
print("wat", c2d.read(3, 9,))