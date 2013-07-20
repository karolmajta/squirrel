import os
import pygame
import math

from game_controller import GameController, ControllerResignException
from settings import ASSETS_PATH, RESOLUTION

STATE_ANGLE = 0
STATE_POWER = 1
STATE_FLIGHT = 2

GRAVITY = 0.001

class Cannon(object):

    def __init__(self):
        pth = os.path.join(ASSETS_PATH, 'island.png')
        self.img = pygame.image.load(os.path.join(ASSETS_PATH, 'E.png'))
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
        pygame.draw.line(
            self.surf,
            pygame.Color(255, 0, 0, 255),
            (200, 350),
            (200+dx, 350-dy),
            10,
        )
        if state != STATE_FLIGHT:
            self.surf.blit(
                self.img,
                (int(200-self.img.get_size()[0]/2), int(350-self.img.get_size()[1]/2))
            )

        if state == STATE_FLIGHT:
            self.surf.set_alpha(int(self.alpha))
        surface.blit(self.surf, (0, 0))

class Squirrel(object):

    def __init__(self):
        self.initial = (200, 350)
        self.actual = (200, 350)
        self.vel = (0, 0)
        self.last_tick = None
        self.images = {
            "N": pygame.image.load(os.path.join(ASSETS_PATH, "N.png")),
            "NE": pygame.image.load(os.path.join(ASSETS_PATH, "NE.png")),
            "E": pygame.image.load(os.path.join(ASSETS_PATH, "E.png")),
            "SE": pygame.image.load(os.path.join(ASSETS_PATH, "SE.png")),
            "S": pygame.image.load(os.path.join(ASSETS_PATH, "S.png")),
        }

    def draw(self, surface, state):
        if state == STATE_FLIGHT:
            if self.vel[1] > 0.6:
                img = self.images["N"]
            elif 0.6 >= self.vel[1] > -0.4:
                img = self.images["NE"]
            elif 0.4 >= self.vel[1] > -0.4:
                img = self.images["E"]
            elif -0.4 >= self.vel[1] > -0.6:
                img = self.images["SE"]
            elif -0.6 >= self.vel[1]:
                img = self.images["S"]
            surface.blit(
                img,
                (int(self.actual[0]-img.get_size()[0]/2), int(self.actual[1]-img.get_size()[1]/2))
            )
    def update(self, surface, state, milis):
        if state == STATE_FLIGHT:
            if self.last_tick is None:
                self.last_tick = milis

            dt = milis-self.last_tick


            dx = dt*self.vel[0]
            dy = dt*self.vel[1]
            print self.vel[1]
            newx = self.actual[0]+dx*0.3 if self.actual[0] < 320 else 320
            self.actual = (newx, self.actual[1]-dy*0.3)

            self.vel = (self.vel[0], self.vel[1]-GRAVITY*dt)

            self.last_tick = milis
class GameplayController(GameController):

    def __init__(self, screen):
        super(GameplayController, self).__init__(screen)
        self.cannon = Cannon()
        self.squirrel = Squirrel()
        self.state = STATE_ANGLE

    def shortpress(self):
        if self.state == STATE_ANGLE:
            self.state = STATE_POWER
            self.cannon.started_at = None
        elif self.state == STATE_POWER:
            self.state = STATE_FLIGHT
            self.cannon.started_at = None
            angle = (self.cannon.angle/360)*2*math.pi
            self.squirrel.vel = (math.sin(angle), math.cos(angle))
        elif self.state == STATE_FLIGHT:
            self.squirrel.vel = (self.squirrel.vel[0], self.squirrel.vel[1]+0.3)

    def longpress(self):
        pass

    def update(self, milis):
        super(GameplayController, self).update(milis)
        self.cannon.update(milis, self.state)
        self.squirrel.update(self.screen, self.state, milis)

    def draw(self):
        super(GameplayController, self).draw()
        self.screen.fill(pygame.Color(255, 255, 255, 255))
        self.cannon.draw(self.screen, self.state)
        self.squirrel.draw(self.screen, self.state)
