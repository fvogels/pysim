import pygame


class MainWindow:
    def __init__(self):
        size = (1920, 1080)
        pygame.display.set_mode(size)

    def process_messages(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
