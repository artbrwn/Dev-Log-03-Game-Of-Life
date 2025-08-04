class Cell:
    def __init__(self, position, neighbours=[], alive=False):
        self.position = position
        self.row = position[0]
        self.col = position[1]
        self.neighbours = neighbours
        self.alive = alive
        self.alive_next_state = None

    def decide_next_state(self):
        alive_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                alive_neighbours += 1
        if self.alive:
            if alive_neighbours >= 2 and alive_neighbours <= 3:
                self.alive_next_state = True
            else:
                self.alive_next_state = False
        else:
            if alive_neighbours == 3:
                self.alive_next_state = True
    
    def update_state(self):
        self.alive = self.alive_next_state

    def get_neighbours(self, grid):
        self.neighbours = []       
        for row_displacement in [-1, 0, 1]:
            for col_displacement in [-1, 0, 1]:
                if row_displacement == 0 and col_displacement == 0:
                    continue
                else:
                    neighbour_row = self.row + row_displacement
                    neighbour_col = self.col + col_displacement

                    if neighbour_row < 0 or neighbour_row >= grid.rows or neighbour_col < 0 or neighbour_col >= grid.cols:
                        continue
                    else:
                        self.neighbours.append(grid.cells[neighbour_row][neighbour_col])

