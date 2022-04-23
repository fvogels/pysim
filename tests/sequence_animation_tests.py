from pysim.graphics.animations.float import LinearFloatAnimation
from pysim.graphics.animations.sequence import SequenceAnimation
from pytest import mark
from pytest import approx


@mark.parametrize("child_durations", [
    [],
    [1],
    [1, 1],
    [1, 1, 1],
    [1, 2],
    [1, 2, 3]
])
def test_duration(child_durations):
    children = [LinearFloatAnimation(0, 1, duration) for duration in child_durations]
    expected = sum(child_durations)
    animation = SequenceAnimation(children)
    assert animation.duration == approx(expected)
