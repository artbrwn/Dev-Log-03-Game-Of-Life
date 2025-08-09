from src.universe import Universe
from src.cell import Cell

def test_create_universe():
    test_universe = Universe()
    len(test_universe.cells) == test_universe.rows

def test_grid_correct_dimensions():
    test_universe = Universe(3, 3)
    assert test_universe.rows == 3
    assert test_universe.cols == 3

def test_cell_knows_position():
    test_universe = Universe()
    test_universe.cells[(0, 0)] = Cell((0, 0), test_universe, alive=True)
    assert test_universe.cells[(0, 0)].position == (0,0)

def test_cell_is_not_self_neighbour():
    test_universe = Universe()
    test_universe.cells[(0, 0)] = Cell((0, 0), test_universe, alive=True)
    test_universe.cells[(0, 0)].explore_universe()
    assert test_universe.cells[(0, 0)] not in test_universe.cells[(0, 0)].neighbours