from abstract_controller import AbstractController
from colors import BLACK

STARTSTATE = 0
INGAMESTATE = 1
ENDGAME = 2


class GameController(AbstractController):

    def __init__(self, screen=None):
        self.screen = screen
        self.state = STARTSTATE

        self.screen.fill(BLACK)

    def longpress(self):
        print 'gamelong'

    def shortpress(self):
        print 'gameshort'
