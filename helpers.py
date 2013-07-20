#functions to create our resources
import os
import pygame
from pygame.compat import geterror

data_dir = 'assets'

def load_image(name, scale=(30,200)):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    image = pygame.transform.scale(image, scale)
    return image, image.get_rect()

