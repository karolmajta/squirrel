import os
import pygame
from abstract_controller import AbstractController
from colors import WHITE
from settings import RESOLUTION


class IntroException(Exception):
    pass


class IntroController(AbstractController):
    assets_dir = 'assets'

    def __init__(self, screen):
        self.intro_images = ['1_intro.png', '2_intro.jpg', '3_intro.jpg', ]
        self.actual = 0
        self.screen = screen
        screen.fill(WHITE)
        self.draw_image("logo.png", (50, 200), False)

    def shortpress(self):
        img_file = self.next()
        self.draw_image(img_file)

    def longpress(self):
        imgfile = self.get_last()
        self.draw_image(imgfile)

    def draw_image(self, img_filename, position=(0, 0), scale=True):
        img_file = pygame.image.load(os.path.join(self.assets_dir, img_filename))
        if scale:
            img_file = pygame.transform.scale(img_file, RESOLUTION)
        self.screen.blit(img_file, position)

    def next(self):
        if self.actual != 3:
            img = self.intro_images[self.actual]
            self.actual += 1
            return img
        else:
            raise IntroException()

    def get_last(self):
        img = self.intro_images[2]
        self.actual = 3
        return img

