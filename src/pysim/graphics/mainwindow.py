import pygame
from pysim.graphics.screen import Screen
from typing import cast


class MainWindow:
    __surface : pygame.Surface
    __clock : pygame.time.Clock
    __screen : Screen

    def __init__(self, initial_screen : Screen):
        size = (1920, 1080)
        self.__surface = cast(pygame.Surface, pygame.display.set_mode(size))
        self.__clock = pygame.time.Clock()
        self.__screen = initial_screen

    @property
    def screen(self) -> Screen:
        return self.__screen

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            elapsed_seconds = self.__clock.tick() / 1000

            self.screen.update(elapsed_seconds)
            self.screen.render(self.__surface)

            pygame.display.flip()
