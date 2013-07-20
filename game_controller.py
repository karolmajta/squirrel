import pygame
from abstract_controller import AbstractController
from block import Block
from cannon import Cannon
from colors import WHITE
from settings import STARTSTATE, INGAMESTATE


class GameController(AbstractController):
    def __init__(self, screen=None):
        self.screen = screen
        self.state = STARTSTATE

        cannon = Cannon()
        cannon.state = self.state

        block = Block()
        block.state = self.state

        self.screen.fill(WHITE)
        self.allsprites = pygame.sprite.RenderPlain((cannon,block))
        self.allsprites.draw(self.screen)

    def update(self):
        if self.state == STARTSTATE:
            self.screen.fill(WHITE)
            self.allsprites.update()

            self.allsprites.draw(self.screen)
            pygame.display.flip()


    def longpress(self):
        print 'gamelong'

    def shortpress(self):
        self.state = INGAMESTATE
        #self.update()
        pass
