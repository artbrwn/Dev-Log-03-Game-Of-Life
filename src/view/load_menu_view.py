import pygame
from src.config import colors

class LoadMenuView:
    def __init__(self, screen, screen_size, button_size):
        self.screen = screen
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.game_files = []
        self.button_size = button_size
        self.close_button = pygame.Rect(self.screen_size[0] - self.button_size - 30, 30, self.button_size, self.button_size)
        self.font = pygame.font.SysFont("arial", int(self.button_size * 0.8))
        self.file_buttons = []

    def draw(self):
        self.screen.fill(colors.BACKGROUND)

        # Draw close button
        pygame.draw.rect(self.screen, (255, 255, 255), self.close_button)

        # Draw game buttons
        for i, (button, _) in enumerate(self.file_buttons):
            pygame.draw.rect(self.screen, (255, 255, 255), button)
            label_surface = self.font.render(str(i), True, (0, 0, 0))
            label_rect = label_surface.get_rect(center=button.center)
            self.screen.blit(label_surface, label_rect)

        pygame.display.flip()
    
    def update_game_file_buttons(self):
        self.file_buttons = []
        spacing = self.button_size // 2
        i = 0
        for file in self.game_files:
            button = pygame.Rect(
                30,
                30 + i * (self.button_size + spacing),
                self.button_size,
                self.button_size
                )
            i += 1
            self.file_buttons.append((button, file))