import os
import pygame

from game_controller import GameController
from settings import ASSETS_PATH


STATE_FADEIN = 0
STATE_DISPLAYIMAGE = 1
STATE_FADEOUT = 2

IMAGES = [
    ('logo.png', (50, 200)),
    ('1_intro.png', (0, 0)),
    ('2_intro.png', (0, 0)),
    ('3_intro.png', (0, 0))
]


class IntroController(GameController):

    def __init__(self, screen, fade=0.1):
        super(IntroController, self).__init__(screen)
        self.state = STATE_FADEIN
        self.opacity = 255
        self.images = map(lambda i: self.load_image(i), IMAGES)
        self.current_image = self.images[0]
        try:
            self.next_image = self.images[1]
        except IndexError:
            self.next_image = None

    def load_image(self, fn):
        pth = os.path.join(ASSETS_PATH, fn[0])
        img = pygame.image.load(pth)
        return (img, fn[1])

    def shortpress(self):
        self.forward()

    def longpress(self):
        self.fast_forward()

    def forward(self):
        self.state = STATE_FADEOUT

    def fast_forward(self):
        self.state = STATE_FADEOUT

    def draw(self):
        super(IntroController, self).draw()
        self.screen.blit(self.current_image[0], self.current_image[1])
        if self.state == STATE_FADEIN:
            pass
        if self.state == STATE_DISPLAYIMAGE:
            pass
        if self.state == STATE_FADEOUT:
            pass
