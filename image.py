from copy import copy
import os
import pygame


class ImageObject(pygame.sprite.Sprite):

    assets_dir = 'assets'
    img_file = None
    orginal_image = None


    def __init__(self, *args, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/arena.jpg", -1)

        self.img_file = pygame.image.load(os.path.join(self.assets_dir, self.img_filename))
        if self.size:
            self.img_file = pygame.transform.scale(self.img_file, self.size)
        self.orginal_image = copy(self.img_file)
        self.rect = self.img_file.get_rect()

    def resize(self, img_file, resize):
        return pygame.transform.scale(img_file, resize)