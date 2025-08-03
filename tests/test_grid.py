from src.grid import Grid

def test_create_grid():
    test_grid = Grid()
    test_grid.build_grid()
    len(test_grid.cells) == test_grid.rows
    test_grid.cells[0][0].row == 0
    test_grid.cells[1][1].col == 1

def test_grid_correct_dimensions():
    grid_test = Grid()
    assert grid_test.rows == 3
    assert grid_test.cols == 3

def test_cell_knows_position():
    grid_test = Grid()
    grid_test.setup()
    assert grid_test.cells[0][0].position == (0,0)
    assert grid_test.cells[2][1].position == (2,1)

def test_3x3_grid_center_cell_has_8_neighbours():
    grid_test = Grid(3, 3)
    grid_test.setup()
    assert len(grid_test.cells[1][1].neighbours) == 8

def test_top_left_corner_only_has_3_neighbours():
    grid_test = Grid()
    grid_test.setup()
    assert len(grid_test.cells[0][0].neighbours) == 3

def test_cell_is_not_self_neighbour():
    grid_test = Grid()
    grid_test.setup()
    assert grid_test.cells[0][0] not in grid_test.cells[0][0].neighbours