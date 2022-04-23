from pysim.data.grid import Grid
from abc import ABC


class Square(ABC):
    pass


class Wall(Square):
    pass


class Empty(Square):
    pass


class World:
    def __init__(self, grid : Grid[Square]):
        self.__grid = grid

    @property
    def grid(self):
        return self.__grid
