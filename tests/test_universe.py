from src.universe import Universe

def test_create_grid():
    test_universe = Universe()
    test_universe.build_grid()
    len(test_universe.cells) == test_universe.rows
    test_universe.cells[0][0].row == 0
    test_universe.cells[1][1].col == 1

def test_grid_correct_dimensions():
    test_universe = Universe()
    assert test_universe.rows == 3
    assert test_universe.cols == 3

def test_cell_knows_position():
    test_universe = Universe()
    test_universe.setup()
    assert test_universe.cells[0][0].position == (0,0)
    assert test_universe.cells[2][1].position == (2,1)

def test_cell_is_not_self_neighbour():
    test_universe = Universe()
    test_universe.setup()
    assert test_universe.cells[0][0] not in test_universe.cells[0][0].neighbours