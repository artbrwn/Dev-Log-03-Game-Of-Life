from src.cell import Cell

class Universe:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.cells = {}

    def setup(self):
        self.build_universe()
        for cell in self.cells.values():
            cell.get_neighbours(self)
    
    def build_universe(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[(i, j)] = Cell((i, j))