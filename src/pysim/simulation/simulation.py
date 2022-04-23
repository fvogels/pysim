from pysim.data.position import Position
from .world import World


class Simulation:
    __world : World
    __position = Position

    def __init__(self, world : World, initial_position : Position):
        self.__world = world
        self.__position = initial_position
