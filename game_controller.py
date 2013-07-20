import os
import pygame
from abstract_controller import AbstractController
from cannon import Cannon
from colors import WHITE
from settings import RESOLUTION

STARTSTATE = 0
INGAMESTATE = 1
ENDGAME = 2


class GameController(AbstractController):
    def __init__(self, screen=None):
        self.screen = screen
        self.state = STARTSTATE
        self.cannon = Cannon()
        self.screen.fill(WHITE)

        self.draw_image(self.cannon, (100, 200), True)

    def update(self):
        self.cannon.rotate_canon()
        self.screen.fill(WHITE)
        self.draw_image(self.cannon, self.cannon.position)

    def longpress(self):
        print 'gamelong'

    def shortpress(self):
        self.update()

    def draw_image(self, obj, position=(0, 0), first= False):
        import ipdb; ipdb.set_trace()
        self.screen.blit(obj.img_file, position).center
