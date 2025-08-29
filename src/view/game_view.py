import pygame
from src.config import colors 

class GameView:
    """
    Handles the graphical representation of the Game of Life universe, 
    including rendering cells, UI elements, and notifications.
    """
    def __init__(self, universe, screen, cell_size=10, navigation_bar_height=50):
            self.universe = universe
            self.cell_size = cell_size
            self.screen_size = (universe.cols * cell_size, universe.rows * cell_size + navigation_bar_height)
            self.screen = screen
            self.navigation_bar_height = navigation_bar_height
            self.button_size = navigation_bar_height - navigation_bar_height * 0.2
            self.buttons = []
            self.button_labels = [">", "||", ">|", "[o]", "[^]"] 
            self.font = pygame.font.SysFont("arial", int(self.button_size * 0.8))
            self.notification = {}
  
            # Coordinate in y of navigation bar bottom left corner
            bar_bot_y = self.universe.rows * self.cell_size + self.navigation_bar_height

            # Spacing between buttons
            spacing = self.button_size // 2
            
            total_buttons_width = 5 * self.button_size + (5 - 1) * spacing

            start_x = (self.universe.cols * self.cell_size - total_buttons_width) // 2

            for i in range(5): 
                button = pygame.Rect(
                    start_x + i * (self.button_size + spacing),
                    bar_bot_y - self.navigation_bar_height // 2 - self.button_size // 2,
                    self.button_size,
                    self.button_size
                )
                
                self.buttons.append(button)
    
    def draw(self):
        """
        Render the game view:
        - Fills the background.
        - Draws all alive cells.
        - Draws the navigation bar with buttons.
        - Displays temporary notifications if any.
        - Updates the display (pygame.display.flip).
        """
        self.screen.fill((colors.BACKGROUND))
        # Draw cells (alive)
        for (row, col) in self.universe.cells:
            cell_rect = pygame.Rect(
                col * self.cell_size,
                row * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, colors.CELL_COLOR, cell_rect)
        # Draw flux control bar below
        bar_rect = pygame.Rect(
            0,
            self.universe.rows * self.cell_size,
            self.universe.cols * self.cell_size,
            self.navigation_bar_height
            )
        pygame.draw.rect(self.screen, (colors.BAR_COLOR), bar_rect)
        
        # Draw pause, play, and next step buttons
        for i, button in enumerate(self.buttons):
            pygame.draw.rect(self.screen, colors.BUTTONS_COLOR, button)
            label_surface = self.font.render(self.button_labels[i], True, colors.BUTTONS_TEXT_COLOR)
            label_rect = label_surface.get_rect(center=button.center)
            self.screen.blit(label_surface, label_rect)
        
        # Draw notification
        if self.notification:
            elapsed = pygame.time.get_ticks() - self.notification["start_time"]
            if elapsed < self.notification["duration"]:
                notification_surface = self.font.render(self.notification["text"], True, colors.NOTIFICATION_COLOR)
                notification_rect = notification_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                self.screen.blit(notification_surface, notification_rect)
        else:
             self.notification = {}

        pygame.display.flip()

        