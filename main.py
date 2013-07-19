import pygame
import sys
import time


def init_game():
    window = pygame.display.set_mode((468, 60))
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pirate Squirrel")
    screen = pygame.display.get_surface()
    return (window, screen)


def shutdown_game(window):
    sys.exit(0)


def mainloop(screen):
    # flip the display
    pygame.display.flip()
    # we need to transform all events from
    # big todo
    time.sleep(2)


if __name__ == "__main__":
    window, screen = init_game()
    mainloop(screen)
    shutdown_game(window)
