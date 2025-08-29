import pygame
from src.config import colors

class LoadMenuView:
    """
    A view responsible for displaying and managing the load menu UI.

    This class handles the rendering of buttons for available game files,
    as well as a close button. It provides a way to update the buttons dynamically
    based on the list of available saved games.
    """
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
        """
        Render the load menu view on the screen.

        This includes:
            - Filling the background.
            - Drawing the close button.
            - Drawing a button for each available game file.
            - Displaying a numeric label for each file button.

        Finally, updates the display using pygame.display.flip().
        """
        self.screen.fill(colors.BAR_COLOR)

        # Draw close button
        pygame.draw.rect(self.screen, colors.BUTTONS_COLOR, self.close_button)

        # Draw game buttons
        for i, (button, _) in enumerate(self.file_buttons):
            pygame.draw.rect(self.screen, colors.BUTTONS_COLOR, button)
            label_surface = self.font.render(str(i), True, (colors.BUTTONS_TEXT_COLOR))
            label_rect = label_surface.get_rect(center=button.center)
            self.screen.blit(label_surface, label_rect)

        pygame.display.flip()
    
    def update_game_file_buttons(self):
        """
        Update the list of file buttons based on the current game files.

        Each button is positioned vertically with spacing, and associated
        with a file from the `game_files` list.

        This method resets the current list of `file_buttons` and rebuilds it.
        """
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