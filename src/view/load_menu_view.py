import pygame
from src.config import colors

class LoadMenuview:
    def __init__(self, screen, screen_size, button_size):
        self.screen = screen
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.game_files = []
        self.button_size = button_size
        self.button = pygame.Rect(self.screen_size[0] - self.button_size - 30, 30, self.button_size, self.button_size)

    def draw(self):
        self.screen.fill(colors.BACKGROUND)

        # Draw close button
        pygame.draw.rect(self.screen, (255, 255, 255), self.button)

        pygame.display.flip()