from src.cell import Cell
import random

class Universe:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.cells = {}
        self.birth_signals = {}
                
    def tick(self):
        for cell in list(self.cells.values()):
            cell.explore_universe()
            cell.decide_next_state()
        
        for cell in list(self.cells.values()):
            cell.apply_next_state()
        
        for position, count in self.birth_signals.items():
            if count == 3:
                self.cells[position] = Cell(position, self)
        
        self.birth_signals.clear()
    
    def seed_random(self, probability):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < probability:
                    position = (row, col)
                    self.cells[position] = Cell(position, self)