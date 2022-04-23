from pysim.graphics.animations.float import LinearFloatAnimation
from pytest import mark
from pytest import approx


@mark.parametrize("start, stop, duration", [(start, stop, duration) for start in range(1, 10) for stop in range(1, 10) for duration in range(1, 10)])
def test_start(start, stop, duration):
    animation = LinearFloatAnimation(start=start, stop=stop, duration=duration)
    assert animation[0] == start


@mark.parametrize("start, stop, duration", [(start, stop, duration) for start in range(1, 10) for stop in range(1, 10) for duration in range(1, 10)])
def test_stop(start, stop, duration):
    animation = LinearFloatAnimation(start=start, stop=stop, duration=duration)
    assert animation[duration] == approx(stop)


@mark.parametrize("start, stop, duration", [(start, stop, duration) for start in range(1, 10) for stop in range(1, 10) for duration in range(1, 10)])
def test_middle(start, stop, duration):
    animation = LinearFloatAnimation(start=start, stop=stop, duration=duration)
    expected = (start + stop) / 2
    assert animation[duration / 2] == approx(expected)