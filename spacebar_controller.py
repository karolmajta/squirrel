import sys

import pygame
from pygame.locals import *
from game_controller import GameController
from intro_controller import IntroException

LONGPRESS = USEREVENT+2
SHORTPRESS = USEREVENT+3

class SpacebarController(object):

    def __init__(self, longpress_min_milis=500, shortpress_max_milis=200, screen=None, controller=None):
        self.longpress_min_milis = longpress_min_milis
        self.shortpress_max_milis = shortpress_max_milis
        self.push_started_at = None
        self.controller = controller
        self.screen = screen

    def tick(self, milis):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                sys.exit(0)  # hack but who cares
            elif event.type == KEYUP:
                self.handle_keyup(event, milis)
            elif event.type == KEYDOWN and event.key == 32:
                self.handle_keydown(event, milis)
            elif event.type == LONGPRESS:
                self.controller.longpress()
            elif event.type == SHORTPRESS:
                try:
                    self.controller.shortpress()
                except IntroException, e:

                    self.controller = GameController(screen=self.controller.screen)

            else:
                continue
        return events

    def handle_keyup(self, ev, milis):
        if self.push_started_at is None:
            return
        else:
            if milis - self.push_started_at > self.longpress_min_milis:
                deadevent = pygame.event.Event(LONGPRESS)
                pygame.event.post(deadevent)
                print "longpress"
            elif milis - self.push_started_at < self.shortpress_max_milis:
                deadevent = pygame.event.Event(SHORTPRESS)
                pygame.event.post(deadevent)
                print "shortpress"
            else:
                # Just pass and don't do anything
                print "press ignored"
            self.push_started_at = None

    def handle_keydown(self, ev, milis):
        if self.push_started_at is None:
            self.push_started_at = milis
