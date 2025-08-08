class Cell:
    def __init__(self, position, neighbours=[], alive=True):
        self.position = position
        self.row = position[0]
        self.col = position[1]
        self.neighbours = neighbours
        self.alive = alive
        self.alive_next_state = None

    def decide_next_state(self):
        """
        Updates self.alive_next_state to true if the cell has 2 or 3 alive neighbours.
        """
        alive_neighbours = len(self.neighbours)
        if alive_neighbours >= 2 and alive_neighbours <= 3:
            self.alive_next_state = True
        else:
            self.alive_next_state = False
    
    def update_state(self):
        """
        Updates self.alive to match the previous self.alive_next_state.
        """
        self.alive = self.alive_next_state

    def get_neighbours(self, universe):
        """
        Updates self.neighbours with only those cells alive in the limits of the actual cell.
        """
        self.neighbours = []       
        for row_displacement in [-1, 0, 1]:
            for col_displacement in [-1, 0, 1]:
                if row_displacement == 0 and col_displacement == 0:
                    continue
                else:
                    neighbour_row = self.row + row_displacement
                    neighbour_col = self.col + col_displacement

                    if neighbour_row < 0 or neighbour_row >= universe.rows or neighbour_col < 0 or neighbour_col >= universe.cols:
                        continue
                    else:
                        neighbour = universe.cells.get((neighbour_row, neighbour_col))
                        if neighbour:
                            self.neighbours.append(neighbour)