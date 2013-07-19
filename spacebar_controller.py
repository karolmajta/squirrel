import sys

import pygame
from pygame.locals import *


class SpacebarController(object):

    def __init__(self, longpress_min_milis=500, shortpress_max_milis=200, controller=None):
        self.longpress_min_milis = longpress_min_milis
        self.shortpress_max_milis = shortpress_max_milis
        self.push_started_at = None
        self.controller = controller

    def tick(self, milis):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                sys.exit(0)  # hack but who cares
            elif event.type == KEYUP:
                self.handle_keyup(event, milis)
            elif event.type == KEYDOWN and event.key == 32:
                self.handle_keydown(event, milis)
            else:
                continue
        return events

    def handle_keyup(self, ev, milis):
        if self.push_started_at is None:
            return
        else:
            if milis - self.push_started_at > self.longpress_min_milis:
                print "longpress"
            elif milis - self.push_started_at < self.shortpress_max_milis:
                print "shortpress"
            else:
                print "press ignored"
            self.push_started_at = None

    def handle_keydown(self, ev, milis):
        if self.push_started_at is None:
            self.push_started_at = milis
