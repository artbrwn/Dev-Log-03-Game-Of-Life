from src.universe import Universe
from src.cell import Cell
import pygame
from src.view.game_view import GameView
import random
from tabulate import tabulate

def main():
    pygame.init()
    main_universe = Universe(50,50)
    view = GameView(main_universe, cell_size=10)
    clock = pygame.time.Clock()

    for row in range(main_universe.rows):
        for col in range(main_universe.cols):
            if random.random() < 0.5:
                position = (row, col)
                main_universe.cells[position] = Cell(position, main_universe)
    running = True
    pause = True
    main_universe.tick()
    view.draw()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if view.buttons[0].collidepoint(event.pos):
                        pause = False
                    elif view.buttons[1].collidepoint(event.pos):
                        pause = True
                    elif view.buttons[2].collidepoint(event.pos):
                        main_universe.tick()
                        view.draw()
                        clock.tick(10)
        if not pause:
            main_universe.tick()
            view.draw()
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