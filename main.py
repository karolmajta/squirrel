import pygame
import sys
import time
from intro_controller import IntroController
from outro_controller import OutroController
from settings import RESOLUTION
from collections import OrderedDict

from spacebar_controller import SpacebarController, LONGPRESS, SHORTPRESS


class GameControllerManager(object):

    def __init__(self, controllers):
        self.controllers = controllers
        self.active_controller = controllers.values()[0]

    def activate(self, name):
        self.active_controller = self.controllers[name]


def init_game():
    window = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Pirate Squirrel")
    screen = pygame.display.get_surface()
    return window, screen


def mainloop(screen, started_at):
    # we need to transform all events from

    sc = SpacebarController()

    game_controllers = OrderedDict({
        "intro": OutroController(screen),
    })
    cm = GameControllerManager(game_controllers)

    while True:
        current_time = time.time()
        time_elapsed = 1000 * (current_time - started_at)
        event = sc.tick(time_elapsed)
        if event: print event

        if event == LONGPRESS:
            cm.active_controller.longpress()
        elif event == SHORTPRESS:
            cm.active_controller.shortpress()

        cm.active_controller.update(time_elapsed)

        # flip the display
        pygame.display.flip()

        cm.active_controller.draw()


if __name__ == "__main__":
    window, screen = init_game()
    start_time = time.time()
    mainloop(screen, start_time)
    sys.exit(0)
