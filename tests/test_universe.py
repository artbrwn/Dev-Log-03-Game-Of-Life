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

def test_universe_initializes_correct_grid():
    u = Universe(4, 6)
    assert u.rows == 4
    assert u.cols == 6

def test_universe_top_left_cell_has_3_neighbours():
    u = Universe(3, 3)
    u.seed_random(1)
    c = u.cells[(0, 0)]
    c.explore_universe()
    assert len(c.neighbours) == 3

def test_universe_bottom_right_cell_has_3_neighbours():
    u = Universe(3, 3)
    u.seed_random(1)
    c = u.cells[(2, 2)]
    c.explore_universe()
    assert len(c.neighbours) == 3

def test_middle_cell_has_8_neighbours():
    u = Universe(3, 3)
    u.seed_random(1)
    c = u.cells[(1, 1)]
    c.explore_universe()
    assert len(c.neighbours) == 8

def test_seed_random_with_zero_probability_creates_no_cells():
    u = Universe(4, 4)
    u.seed_random(0.0)
    assert len(u.cells) == 0


def test_seed_random_with_one_probability_fills_whole_grid():
    u = Universe(4, 4)
    u.seed_random(1.0)
    assert len(u.cells) == u.rows * u.cols

def test_birth_occurs_with_exactly_three_signals():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(0, 1), (0, 2), (1, 2)]}
    u.tick()
    assert (1, 1) in u.cells

def test_birth_occurs_with_exactly_three_signals():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(0, 1), (0, 2), (1, 2)]}
    u.tick()
    assert (1, 1) in u.cells

def test_no_birth_with_two_signals():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(0, 1), (1, 2)]}
    u.tick()
    assert (1, 1) not in u.cells

def test_live_cell_survives_with_two_neighbours():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(1, 1), (1, 2), (2, 1)]}
    u.tick()
    assert (1, 1) in u.cells

def test_live_cell_dies_with_one_neighbour():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(1, 1), (1, 2)]}
    u.tick()
    assert (1, 1) not in u.cells
    assert (1, 2) not in u.cells

def test_live_cell_dies_with_more_than_three_neighbours():
    u = Universe(3, 3)
    u.cells = {pos: Cell(pos, u) for pos in [(1, 1), (0, 1), (1, 0), (1, 2), (2, 1)]}
    u.tick()
    assert (1, 1) not in u.cells