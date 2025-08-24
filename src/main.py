import pygame
import random
from tabulate import tabulate
from src.universe import Universe
from src.cell import Cell
from src.view.game_view import GameView
from src.persistence import Persistence
from src.view.load_menu_view import LoadMenuview

def main():
    pygame.init()
    main_universe = Universe(50,50)
    screen = pygame.display.set_mode((800, 600))
    game_view = GameView(main_universe, cell_size=10, screen=screen)
    clock = pygame.time.Clock()
    persistence = Persistence(main_universe)
    load_menu_view = LoadMenuview(screen, game_view.screen_size, game_view.button_size)

    

    for row in range(main_universe.rows):
        for col in range(main_universe.cols):
            if random.random() < 0.5:
                position = (row, col)
                main_universe.cells[position] = Cell(position, main_universe)
    running = True
    pause = True
    state = "game"
    main_universe.tick()
    game_view.draw()
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if state == "game":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if game_view.buttons[0].collidepoint(event.pos):
                            pause = False
                        elif game_view.buttons[1].collidepoint(event.pos):
                            pause = True
                        elif game_view.buttons[2].collidepoint(event.pos):
                            main_universe.tick()
                            game_view.draw()
                            clock.tick(10)
                        elif game_view.buttons[3].collidepoint(event.pos):
                            persistence.save_state(main_universe)
                            game_view.notification = {"text": "Saved!", "start_time": pygame.time.get_ticks(), "duration": 1500}
                        elif game_view.buttons[4].collidepoint(event.pos):
                            state = "menu_load"
            if not pause:
                main_universe.tick()
                
            game_view.draw()

        elif state == "menu_load":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if load_menu_view.close_button.collidepoint(event.pos):
                            state = "game"

            game_files = persistence.load_game_files_names()
            load_menu_view.game_files = game_files
            load_menu_view.update_game_file_buttons()
            load_menu_view.draw()
        clock.tick(10)
    
    pygame.quit()

def write_in_console(universe):
    grid = []
    for y in range(universe.rows):
        row = []
        for x in range(universe.cols):
            row.append("O" if (x, y) in universe.cells else ".")
        grid.append(row)
    print(tabulate(grid, tablefmt="grid"))

if __name__ == "__main__":
    main()