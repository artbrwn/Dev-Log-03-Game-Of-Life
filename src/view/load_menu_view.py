import pygame

class LoadMenuview:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw(self):
        self.screen.fill(("#2B332B"))
        