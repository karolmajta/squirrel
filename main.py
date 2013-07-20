import pygame
import sys
import time
from intro_controller import IntroController
from settings import RESOLUTION

from spacebar_controller import SpacebarController


def init_game():
    window = pygame.display.set_mode((468, 60))
    pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Pirate Squirrel")
    screen = pygame.display.get_surface()
    return window, screen


def mainloop(screen, started_at):
    # we need to transform all events from

    intro = IntroController(screen)
    sc = SpacebarController(controller=intro)
    clock = pygame.time.Clock()
    while True:
        clock.tick(50)
        current_time = time.time()
        time_elapsed = 1000 * (current_time - started_at)
        sc.tick(time_elapsed)

        # flip the display
        pygame.display.flip()


if __name__ == "__main__":
    window, screen = init_game()
    start_time = time.time()
    mainloop(screen, start_time)
    sys.exit(0)
