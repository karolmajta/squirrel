import pygame
import sys
import time

from spacebar_controller import SpacebarController


def init_game():
    window = pygame.display.set_mode((468, 60))
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pirate Squirrel")
    screen = pygame.display.get_surface()
    return (window, screen)


def mainloop(screen, started_at):
    # we need to transform all events from

    sc = SpacebarController()

    while(True):
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
