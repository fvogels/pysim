from typing import TypeVar, Generic, Callable
from pysim.data.position import Position


T = TypeVar('T')


class Grid(Generic[T]):
    __contents : list[list[T]]

    def __init__(self, width, height, initializer : Callable[[Position], T]):
        self.__contents = [[initializer(Position(x, y)) for x in range(width)] for y in range(height)]

    def __getitem__(self, position : Position) -> T:
        return self.__contents[position.y][position.x]

    @property
    def width(self) -> int:
        return len(self.__contents[0])

    @property
    def height(self) -> int:
        return len(self.__contents)
