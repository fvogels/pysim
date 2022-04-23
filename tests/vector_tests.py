from pysim.data.vector import Vector
from pytest import mark


@mark.parametrize('x, y', [(x, y) for x in range(-5, 5) for y in range(-5, 5)])
def test_cw_eq_3ccw(x, y):
    vector = Vector(x, y)
    assert vector.rotate_clockwise() == vector.rotate_counterclockwise().rotate_counterclockwise().rotate_counterclockwise()
