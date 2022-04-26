from pysim.data.grid import Grid
from pysim.data.vector import Vector
from abc import ABC


class Tile(ABC):
    pass


class Wall(Tile):
    pass


class Empty(Tile):
    pass


class World:
    def __init__(self, grid : Grid[Tile]):
        self.__grid = grid

    @property
    def width(self) -> int:
        return self.__grid.width

    @property
    def height(self) -> int:
        return self.__grid.height

    def __getitem__(self, position : Vector) -> Tile:
        return self.__grid[position]
