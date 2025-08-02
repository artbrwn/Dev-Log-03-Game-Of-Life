from src.cell import Cell

def test_cell_creation():
    test_cell = Cell([0, 0], [None, None, None, None, None, None, None, None])
    assert test_cell

def test_update_state():
    target_cell = Cell([0, 0], 
                       [Cell([1, 1], [], alive=True), 
                       Cell([2, 2], [], alive=True), 
                       Cell([3, 3], [], alive=True)])
    assert not target_cell.alive
    target_cell.decide_next_state()
    target_cell.update_state()
    assert target_cell.alive

    