from src.cell import Cell
import random

class Universe:
    """
    Represents the Game of Life universe where cells evolve autonomously.
    
    Unlike traditional implementations, the universe does not directly
    determine births and deaths. Instead, each Cell explores its surroundings,
    decides its own fate, and collaborates with others to signal new births.
    """

    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.cells = {}
        self.birth_signals = {}
                
    def tick(self):
        """
        Advance the universe by one generation.
        
        Process overview:
            1. Each cell explores its neighborhood and decides its next state.
            2. Each cell applies its decided state (survival or death).
            3. New cells are created at positions that received exactly 3 birth signals.
            4. Birth signals are cleared for the next tick.
        """
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
        """
        Randomly populate the universe with living cells.

        Args:
            probability (float): Probability (0.0–1.0) that a given grid position
                                 starts with a living cell.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < probability:
                    position = (row, col)
                    self.cells[position] = Cell(position, self)