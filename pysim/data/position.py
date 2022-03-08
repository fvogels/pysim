from typing import Any


class Position:
    def __init__(self, x : int, y : int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __eq__(self, other : Any) -> bool:
        return isinstance(other, Position) and self.x == other.x and self.y == other.y
