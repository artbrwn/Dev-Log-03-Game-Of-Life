import pygame

class GameView:
    def __init__(self, universe, cell_size=10, navigation_bar_height=50):
            self.universe = universe
            self.cell_size = cell_size
            self.screen = pygame.display.set_mode(
                (universe.cols * cell_size, universe.rows * cell_size + navigation_bar_height)
                )
            self.navigation_bar_height = navigation_bar_height
            self.button_size = navigation_bar_height - navigation_bar_height * 0.2
            self.buttons = []
            self.button_labels = [">", "||", ">|", "[o]"]
            self.font = pygame.font.SysFont("arial", int(self.button_size * 0.8))


            # Coordinate in y of navigation bar bottom left corner
            bar_bot_y = self.universe.rows * self.cell_size + self.navigation_bar_height

            # Spacing between buttons
            spacing = self.button_size // 2
            
            total_buttons_width = 4 * self.button_size + (4 - 1) * spacing

            start_x = (self.universe.cols * self.cell_size - total_buttons_width) // 2

            for i in range(4): 
                button = pygame.Rect(
                    start_x + i * (self.button_size + spacing),
                    bar_bot_y - self.navigation_bar_height // 2 - self.button_size // 2,
                    self.button_size,
                    self.button_size
                )
                
                self.buttons.append(button)
    
    def draw(self):
        self.screen.fill(("#2B332B"))
        # Draw cells (alive)
        for (row, col) in self.universe.cells:
            cell_rect = pygame.Rect(
                col * self.cell_size,
                row * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, (0, 255, 0), cell_rect)
        # Draw flux control bar below
        bar_rect = pygame.Rect(
            0,
            self.universe.rows * self.cell_size,
            self.universe.cols * self.cell_size,
            self.navigation_bar_height
            )
        pygame.draw.rect(self.screen, ("#395539"), bar_rect)
        
        # Draw pause, play, and next step buttons
        for i, button in enumerate(self.buttons):
            pygame.draw.rect(self.screen, (255, 255, 255), button)
            label_surface = self.font.render(self.button_labels[i], True, (0, 0, 0))
            label_rect = label_surface.get_rect(center=button.center)
            self.screen.blit(label_surface, label_rect)
        pygame.display.flip()