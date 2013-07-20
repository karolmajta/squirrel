import os
import pygame
import math

from game_controller import GameController, ControllerResignException
from settings import ASSETS_PATH, RESOLUTION

STATE_ANGLE = 0
STATE_POWER = 1
STATE_FLIGHT = 2


class Cannon(object):

    def __init__(self):
        pth = os.path.join(ASSETS_PATH, 'island.png')
        self.image = pygame.image.load(pth)
        self.anglerange = (10, 80)
        self.angle = 10
        self.surf = pygame.Surface((640, 480))
        self.started_at = None
        self.line_width = 100
        self.recorded_angle = None
        self.alpha = 255

    def update(self, milis, state):
        if self.started_at is None:
            self.started_at = milis
        time_elapsed = milis - self.started_at
        if state == STATE_ANGLE:
            ad = self.anglerange[1] - self.anglerange[0]
            self.angle = 35+70*math.sin(time_elapsed/200)
        if state == STATE_POWER:
            self.line_width = 100 + 100*math.sin(time_elapsed/100)
        if state == STATE_FLIGHT:
            self.alpha = max(0, 255-time_elapsed)

    def draw(self, surface, state):
        self.surf.fill(pygame.Color(255, 255, 255, 255))
        self.surf.blit(self.image, (0, 70))
        dx = self.line_width*math.sin(self.angle/360*2*math.pi)
        dy = self.line_width*math.cos(self.angle/360*2*math.pi)
        pygame.draw.line(
            self.surf,
            pygame.Color(255, 0, 0, 255),
            (200, 350),
            (200+dx, 350-dy),
            10,
        )
        pygame.draw.circle(
            self.surf,
            pygame.Color(255, 255, 255, 255),
            (200, 350),
            40,
            0
        )
        pygame.draw.circle(
            self.surf,
            pygame.Color(0, 0, 0, 255),
            (200, 350),
            40,
            5
        )
        if state == STATE_FLIGHT:
            print self.alpha
            self.surf.set_alpha(int(self.alpha))
        surface.blit(self.surf, (0, 0))

class GameplayController(GameController):

    def __init__(self, screen):
        super(GameplayController, self).__init__(screen)
        self.cannon = Cannon()
        self.state = STATE_ANGLE

    def shortpress(self):
        if self.state == STATE_ANGLE:
            self.state = STATE_POWER
            self.cannon.started_at = None
        elif self.state == STATE_POWER:
            self.state = STATE_FLIGHT
            self.cannon.started_at = None

    def longpress(self):
        pass

    def update(self, milis):
        super(GameplayController, self).update(milis)
        self.cannon.update(milis, self.state)

    def draw(self):
        super(GameplayController, self).draw()
        self.screen.fill(pygame.Color(255, 255, 255, 255))
        self.cannon.draw(self.screen, self.state)
