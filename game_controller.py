import pygame


DEFAULT_BLIT_COLOR = pygame.Color(0, 0, 0, 255)


class ControllerResignException(Exception):
    pass


class GameController(object):

    def __init__(self, screen):
        self.screen = screen

    def resign(self):
        raise ControllerResignException()

    def update(self, milis):
        pass

    def longpress(self):
        pass

    def shortpress(self):
        pass

    def draw(self):
        self.screen.fill(DEFAULT_BLIT_COLOR)
