from src.cell import Cell

class Grid:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.cells = []

    def setup(self):
        self.build_grid()
        for row in self.cells:
            for cell in row:
                cell.get_neighbours(self)
    
    def build_grid(self):
        for i in range(self.rows):
            row_cells = []
            for j in range(self.cols):
                row_cells.append(Cell((i, j)))
            self.cells.append(row_cells)