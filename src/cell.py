class Cell:
    def __init__(self, position, universe, neighbours=[], alive=False):
        self.position = position
        self.row = position[0]
        self.col = position[1]
        self.universe = universe
        self.neighbours = neighbours
        self.alive = alive
        self.alive_next_state = None

    def decide_next_state(self):
        """
        Updates self.alive_next_state to true if the cell has 2 or 3 alive neighbours.
        """
        alive_neighbours = len(self.neighbours)
        if alive_neighbours == 2 or alive_neighbours == 3:
            self.alive_next_state = True
        else:
            self.alive_next_state = False

    def explore_universe(self):
        """
        Iterates over a cell's surroundings. If there's a living cell, it adds it as its neighbour. 
        If there's not, it emits a birth signal for those positions.
        """
        self.neighbours = []
        for row_displacement in [-1, 0, 1]:
            for col_displacement in [-1, 0, 1]:
                if row_displacement == 0 and col_displacement == 0:
                    continue
                else:
                    neighbour_row = self.row + row_displacement
                    neighbour_col = self.col + col_displacement

                    if neighbour_row < 0 or neighbour_row >= self.universe.rows or neighbour_col < 0 or neighbour_col >= self.universe.cols:
                        continue
                    else:
                        neighbour = self.universe.cells.get((neighbour_row, neighbour_col))
                        if neighbour:
                            self.neighbours.append(neighbour)
                        else:
                            self.emit_birth_signal(self.universe, (neighbour_row, neighbour_col))

    def emit_birth_signal(self, universe, position):
        if position in universe.birth_signals:
            universe.birth_signals[position] += 1
        else:
            universe.birth_signals[position] = 1

    def apply_next_state(self):
        if not self.alive_next_state:
            del self.universe.cells[self.position]