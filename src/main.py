from src.universe import Universe
from src.cell import Cell
import random
from tabulate import tabulate

def main():
    main_universe = Universe()
    # main_universe.setup()
    for row in range(main_universe.rows):
        for col in range(main_universe.cols):
            if random.random() < 0.5:
                position = (row, col)
                main_universe.cells[position] = Cell(position, main_universe)
    while True:
        main_universe.tick()
        write_in_console(main_universe)
        keep = input("Press enter if you want to continue or send any other letter to exit: ")
        if keep != "":
            break

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