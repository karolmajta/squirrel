import os
import pygame

from game_controller import GameController, ControllerResignException
from settings import ASSETS_PATH, RESOLUTION

STATE_FADEIN = 0
STATE_DISPLAYIMAGE = 1
STATE_FADEOUT = 2

IMAGES = [
    ('logo.png', (50, 200), False),
    ('1_intro.png', (0, 0), True),
    ('2_intro.png', (0, 0), True),
    ('3_intro.png', (0, 0), True)
]
# (filename, position, scale)

class IntroController(GameController):

    def __init__(self, screen, fade=0.3, display_countdown=100000):
        super(IntroController, self).__init__(screen)
        self.last_tick = None
        self.state = STATE_FADEIN
        self.opacity = 255
        self.fade = fade
        self.display_countdown = 1000
        self.countdown_started_at = None
        self.images = map(lambda i: self.load_image(i), IMAGES)
        self.current_image = self.images[0]
        self.next_image_index = 0
        self.ff = False
        self.overlay_surface = pygame.Surface(RESOLUTION)

    def load_image(self, fn):
        pth = os.path.join(ASSETS_PATH, fn[0])
        img = pygame.image.load(pth)
        if fn[2]:
            img = pygame.transform.scale(img, RESOLUTION)
        return (img, fn[1])

    def shortpress(self):
        self.next_image_index += 1
        self.forward()

    def longpress(self):
        if self.next_image_index == len(self.images) - 1:
            self.next_image_index += 1
        else:
            self.next_image_index = len(self.images) - 1
        self.forward()

    def forward(self):
        self.state = STATE_FADEOUT

    def update(self, milis):
        super(IntroController, self).update(milis)
        if self.last_tick is None:
            self.last_tick = milis
        dt = milis - self.last_tick
        if self.state == STATE_FADEIN:
            next_opacity = max(0, self.opacity - self.fade * dt)
            self.opacity = next_opacity
            if self.opacity == 0:
                self.state = STATE_DISPLAYIMAGE
        if self.state == STATE_DISPLAYIMAGE:
            if self.countdown_started_at is None:
                self.countdown_started_at = milis
            if (milis - self.countdown_started_at) > self.display_countdown:
                self.next_image_index += 1
                self.state = STATE_FADEOUT
                self.countdown_started_at = None
        if self.state == STATE_FADEOUT:
            next_opacity = min(255, self.opacity + self.fade * dt)
            self.opacity = next_opacity
            if self.opacity == 255:
                self.forward()
                try:
                    self.current_image = self.images[self.next_image_index]
                except IndexError:
                    raise ControllerResignException()
                self.state = STATE_FADEIN
        self.last_tick = milis

    def draw(self):
        super(IntroController, self).draw()
        self.screen.blit(self.current_image[0], self.current_image[1])
        if self.state in [STATE_FADEIN, STATE_FADEOUT]:
            overlay_color = pygame.Color(0, 0, 0)
            self.overlay_surface.set_alpha(self.opacity)
            self.overlay_surface.fill(overlay_color)
            self.screen.blit(self.overlay_surface, (0, 0))
