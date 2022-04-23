from __future__ import annotations


class Vector:
    __x : int
    __y : int

    def __init__(self, x : int, y : int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def rotate_clockwise(self) -> Vector:
        x = self.__y
        y = -self.__x
        return Vector(x, y)

    def rotate_counterclockwise(self) -> Vector:
        x = -self.__y
        y = self.__x
        return Vector(x, y)

    def __add__(self, other : Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __eq__(self, other : object) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y
