from pysim.graphics.mainwindow import MainWindow
from pysim.graphics.screen import Screen
from pysim.world.world import World
import pygame


class TestScreen(Screen):
    def __init__(self):
        pass

    def update(self, elapsed_seconds : float) -> None:
        pass

    def render(self, surface : pygame.Surface) -> None:
        self.__clear_screen(surface)

    def __clear_screen(self, surface : pygame.Surface) -> None:
        black = (0, 0, 0)
        surface.fill(black)


# class State:
#     __position : Vector2
#     __world : World

#     def __init__(self, world : World, initial_position : Vector2):
#         self.__position = initial_position
#         self.__world = world


def main():
    screen = TestScreen()
    window = MainWindow(screen)
    window.run()


if __name__ == '__main__':
    main()
