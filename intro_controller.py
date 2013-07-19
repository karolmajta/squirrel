import pygame

from colors import WHITE, BLACK


class IntroException(Exception):
    pass


class IntroController(object):
    assets_dir = 'assets/'

    def __init__(self, screen):
        self.intro_images = ['1.png', '2.png', '3.png', ]
        self.actual = 0
        self.screen = screen

    def shortpress(self):
        img_file = self.next()
        self.screen.fill(WHITE)
        pass


    def longpress(self):
        self.screen.fill(BLACK)

    def draw_image(self):
        pygame.draw.rect()


    def next(self):
        if self.actual != 3:
            yield self.intro_images[self.actual]
            self.actual += 1
        else:
            raise StopIteration()



