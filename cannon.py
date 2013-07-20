import os
import pygame
from image import ImageObject


class Cannon(ImageObject):

    position = (100, 200)
    size = (40, 200)
    img_filename = 'rocket.png'
    angle = 90
    param = -10

    def rotate_canon(self):
        oldCenter = self.rect.center
        #rotate surf by DEGREE amount degrees
        self.img_file = pygame.transform.rotate(self.img_file, self.param)

        #get the rect of the rotated surf and set it's center to the oldCenter
        self.rect = self.img_file.get_rect()
        self.rect.center = oldCenter

        self.angle += self.param
        print "angle : %s" %self.angle
        print "param : %s" %self.param

        if self.angle >= 90:
            self.param = -10
        elif self.angle <= 0:
            self.param = 10

