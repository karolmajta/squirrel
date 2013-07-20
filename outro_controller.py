import os
import pygame
from colors import WHITE

from game_controller import GameController
from settings import ASSETS_PATH

BACKGROUND_IMAGE = ''

BOLD = 0
ITALIC = 1

TEXT = [
    ("Squirrel Pirate", [200, 550], 42, [BOLD, ITALIC]), # position will be changing over time
    ("Credits", [200, 600], 15, [BOLD]), # position will be changing over time
    ("next text", [200, 650], 15, [ITALIC]), # position will be changing over time
    ("and last text", [200, 700], 15, [ITALIC]), # position will be changing over time

]

SCROLLING = 0
STOP = 1


class OutroController(GameController):
    def __init__(self, screen):
        super(OutroController, self).__init__(screen)
        self.state = SCROLLING
        self.opacity = 255
        pygame.font.init()
        self.text_list = map(lambda i: self.load_text(i), TEXT)

    def load_text(self, fn):
        myfont = pygame.font.SysFont("Arial", fn[2])
        if BOLD in fn[3]: myfont.set_bold(True)
        if ITALIC in fn[3]: myfont.set_italic(True)

        label = myfont.render(fn[0], 1, (0, 0, 0))

        return label, fn[1], fn[2]

    def shortpress(self):
        self.switch_state()

    def longpress(self):
        # TODO ?
        # Maybe just pass that
        self.switch_state()

    def switch_state(self):
        self.state = STOP if self.state == SCROLLING else SCROLLING

    def update(self, milis):
        if self.state == SCROLLING:
            for text in self.text_list:
                text[1][1] = text[1][1] - 0.1


    def draw(self):
        super(OutroController, self).draw()
        self.screen.fill(WHITE)
        for text in self.text_list:
            self.screen.blit(text[0], text[1])
