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
                self.assign_neighbours(cell)
    
    def build_grid(self):
        for i in range(self.rows):
            row_cells = []
            for j in range(self.cols):
                row_cells.append(Cell((i, j)))
            self.cells.append(row_cells)

    def assign_neighbours(self, cell):
        
        actual_row, actual_col = cell.position       
        neighbours = []
        for row_displacement in [-1, 0, 1]:
            for col_displacement in [-1, 0, 1]:
                if row_displacement == 0 and col_displacement == 0:
                    continue
                else:
                    neighbour_row = actual_row + row_displacement
                    neighbour_col = actual_col + col_displacement

                    if neighbour_row < 0 or neighbour_row >= self.rows or neighbour_col < 0 or neighbour_col >= self.cols:
                        continue
                    else:
                        neighbours.append(self.cells[neighbour_row][neighbour_col])
            
        cell.neighbours = neighbours