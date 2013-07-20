import sys

import pygame
from pygame.locals import *
from game_controller import GameController

LONGPRESS = USEREVENT + 2
SHORTPRESS = USEREVENT + 3


class SpacebarController(object):

    def __init__(self, longpress_min_milis=500, shortpress_max_milis=200):
        self.longpress_min_milis = longpress_min_milis
        self.shortpress_max_milis = shortpress_max_milis
        self.push_started_at = None

    def tick(self, milis):
        events = pygame.event.get()
        press = None
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)  # hack but who cares
            elif event.type == KEYUP:
                press = self.handle_keyup(event, milis)
            elif event.type == KEYDOWN and event.key == 32:
                self.handle_keydown(event, milis)
            else:
                continue

        return press

    def handle_keyup(self, ev, milis):
        press = None
        if self.push_started_at is not None:
            if milis - self.push_started_at > self.longpress_min_milis:
                press = LONGPRESS
            elif milis - self.push_started_at < self.shortpress_max_milis:
                press = SHORTPRESS
            else:
                pass
            self.push_started_at = None
        return press

    def handle_keydown(self, ev, milis):
        if self.push_started_at is None:
            self.push_started_at = milis
