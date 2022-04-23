from pysim.data.grid import Grid
from pysim.data.position import Position
import pytest


@pytest.mark.parametrize("width, height", [(w, h) for w in range(1, 10) for h in range(1, 10)])
def test_size(width, height):
    grid = Grid(width, height, lambda p: None)
    assert grid.width == width
    assert grid.height == height
