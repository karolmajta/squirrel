import os
import pygame
from helpers import load_image
from settings import STARTSTATE


class Cannon(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('rocket.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 40, 310
        self.move = 9
        self.angle = -90
        self.dir = -5
        self.original = self.image

    def update(self):
        "walk or spin, depending on the monkeys state"
        if self.state == STARTSTATE:
            self._spin()


    def _spin(self):
        "spin the monkey image"
        center = self.rect.center
        self.angle = self.angle + self.dir
        if self.angle >= 360:
            self.angle = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.angle)

        if self.angle <= -90:
            self.dir = 5
        elif self.angle >=0:
            self.dir = -5

        self.rect = self.image.get_rect(center=center)


