import pygame
from pygame.locals import *


class BombDisplay(pygame.sprite.Sprite):

    def __init__(self, sprite, scale):
        # Définit le sprite du stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Mise à l'échelle du sprite:
        self.new_scale = (round(self.rect.width * scale),
                          round(self.rect.height * scale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()
