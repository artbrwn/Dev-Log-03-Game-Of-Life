from src.cell import Cell
from src.universe import Universe

def test_cell_starts_dead_by_default():
    c = Cell((1, 1), Universe())
    assert not c.alive

def test_cell_can_be_alive_on_creation():
    c = Cell((2, 3), Universe(), alive=True)
    assert c.alive

def test_cell_knows_position():
    u = Universe(5, 5)
    c = Cell((2, 2), u)
    assert c.position == (2, 2)

def test_cell_explore_finds_neighbours():
    u = Universe(3, 3)
    u.seed_random(1)
    u.cells[(1, 1)].explore_universe()
    neighbours = u.cells[(1, 1)].neighbours
    assert len(neighbours) == 8  

def test_cell_does_not_include_itself_as_neighbour():
    u = Universe(3, 3)
    u.seed_random(1)
    c = u.cells[(1, 1)]
    c.explore_universe()
    assert c not in c.neighbours
    