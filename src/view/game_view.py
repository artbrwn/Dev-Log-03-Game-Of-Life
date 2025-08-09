import pygame

class GameView:
    def __init__(self, universe, cell_size=10):
            self.universe = universe
            self.cell_size = cell_size
            self.screen = pygame.display.set_mode(
                (universe.cols * cell_size, universe.rows * cell_size)
        )
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for (row, col) in self.universe.cells:
            rect = pygame.Rect(
                col * self.cell_size,
                row * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, (0, 255, 0), rect)
        pygame.display.flip()