# -*- coding: utf-8 -*-
import os
import pygame
from colors import WHITE

from game_controller import GameController
from settings import ASSETS_PATH

BACKGROUND_IMAGE = 'outro.png'

BOLD = 0
ITALIC = 1


# (text, start_position, font_size, BOLD/ITALIC, color)
TEXT = [
    ("Squirrel Pirate", [150, 450], 42, [BOLD, ITALIC], (0,0,0)), # position will be changing over time
    ("Credits", [150, 520], 15, [BOLD], (0,255,0)), # position will be changing over time
    ("Code by Karol Majta @karojmajta", [150, 550], 15, [ITALIC], (255,0,0)), # position will be changing over time
    ("Graphic Design by Michał and Oskar", [150, 600], 15, [ITALIC], (255,0,0)), # position will be changing over time
    ("Learning new things by Kamil Gałuszka", [150, 650], 15, [ITALIC], (255,0,0)), # position will be changing over time
]

SCROLLING = 0
STOP = 1


class OutroController(GameController):
    def __init__(self, screen):
        super(OutroController, self).__init__(screen)
        self.state = SCROLLING
        self.opacity = 0
        pygame.font.init()
        self.text_list = map(lambda i: self.load_text(i), TEXT)

    def load_text(self, fn):
        myfont = pygame.font.SysFont("arial", fn[2])
        if BOLD in fn[3]: myfont.set_bold(True)
        if ITALIC in fn[3]: myfont.set_italic(True)
        
        label = myfont.render(fn[0], 1, fn[4])

        return label, fn[1], fn[2]

    def load_background(self):
        pth = os.path.join(ASSETS_PATH, BACKGROUND_IMAGE)
        img = pygame.image.load(pth)
        self.screen.blit(img, (0,0))


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
                text[1][1] = text[1][1] - 0.5


    def draw(self):
        super(OutroController, self).draw()
        self.load_background()
        #self.screen.fill(WHITE)
        for text in self.text_list:
            self.screen.blit(text[0], text[1])
