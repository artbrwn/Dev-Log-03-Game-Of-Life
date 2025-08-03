from src.cell import Cell
from src.grid import Grid

def test_cell_creation():
    test_cell = Cell([0, 0], [])
    assert test_cell

def test_update_state_alive():
    target_cell = Cell([0, 0], 
                       [Cell((0, 1), [], alive=True), 
                       Cell((1, 0), [], alive=True), 
                       Cell((1, 1), [], alive=True)])
    assert not target_cell.alive
    target_cell.decide_next_state()
    target_cell.update_state()
    assert target_cell.alive

def test_update_state_dead():
    target_cell = Cell((0, 0), 
                       [Cell((0, 1), []), 
                       Cell((1, 0), []), 
                       Cell((1, 1), [])])
    assert not target_cell.alive
    target_cell.decide_next_state()
    target_cell.update_state()
    assert not target_cell.alive

def test_create_grid():
    test_grid = Grid()
    test_grid.build_grid()
    len(test_grid.cells) == test_grid.rows
    test_grid.cells[0][0].row == 0
    test_grid.cells[1][1].col == 1