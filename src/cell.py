class Cell:
    def __init__(self, position, neighbours=[], alive=False):
        self.row = position[0]
        self.col = position[1]
        self.neighbours = neighbours
        self.alive = alive
        self.alive_next_state = None

    def decide_next_state(self):
        accum = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                accum += 1
        
        if accum >= 3:
            self.alive_next_state = True
        else:
            self.alive_next_state = False
    
    def update_state(self):
        self.alive = self.alive_next_state